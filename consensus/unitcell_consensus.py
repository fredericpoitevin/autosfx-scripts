import sys
sys.path.append("/project/projectdirs/lcls/SFX_automation/consensus/autosfx/scripts")
import os
import numpy as np
import subprocess
import evaluateIndexing as ei 
import sys
import argparse
from cctbx import uctbx
from cctbx import crystal
import collections
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy import signal
import subprocess
import stat

expName = 'cxic0415'# cxic0415 cxih0115 cxid9114 cxi78513
runNum = 101 # (47, 95, 101) (21) (101) (14)
runStr = str(runNum).zfill(4)
myPath = '/project/projectdirs/lcls/exp/cxi/cxic0515/scratch/old'
streamfile = os.path.join(myPath,expName+'_'+runStr+'.stream')
atol = 0.9 # unitcell values considered close enough (Angstrom and deg)
binSize = 0.1
snr_max = 10
doPlot = False

rankName = expName+"_rank.txt"
if os.path.exists(rankName):
    os.remove(rankName)

spacegroup_guess = collections.defaultdict(list)
spacegroup_guess["triclinic_P"]="P1"
spacegroup_guess["monoclinic_P"]="P2"
spacegroup_guess["monoclinic_C"]="C2"
spacegroup_guess["orthorhombic_P"]="P222"
spacegroup_guess["orthorhombic_C"]="C222"
spacegroup_guess["orthorhombic_F"]="F222"
spacegroup_guess["orthorhombic_I"]="I222"
spacegroup_guess["tetragonal_P"]="P4"
spacegroup_guess["tetragonal_I"]="I4"
spacegroup_guess["rhombohedral_R"]="R3"
spacegroup_guess["hexagonal_P"]="P3"
spacegroup_guess["cubic_P"]="P23"
spacegroup_guess["cubic_F"]="F23"
spacegroup_guess["cubic_I"]="I23"

def write_cell(fname, bravais, unitcell):
    if not fname.endswith(".cell"):
        fname += ".cell" 
    str1 = "CrystFEL unit cell file version 1.0\n"
    str2 = "lattice_type = "+ bravais[0]+ "\n"
    str3 = "centering = "+ bravais[1]+ "\n"
    str4 = "unique_axis = "+ bravais[2]+ "\n"
    str5 = "a = "+ str(float("{:.3f}".format(unitcell[0])))+ " A\n"
    str6 = "b = "+ str(float("{:.3f}".format(unitcell[1])))+ " A\n"
    str7 = "c = "+ str(float("{:.3f}".format(unitcell[2])))+ " A\n"
    str8 = "al = "+ str(float("{:.3f}".format(unitcell[3])))+ " deg\n"
    str9 = "be = "+ str(float("{:.3f}".format(unitcell[4])))+ " deg\n"
    str10 = "ga = "+ str(float("{:.3f}".format(unitcell[5])))+ " deg\n"
    with open(fname,"w") as f:
        L = [str1, str2, str3, str4, str5, str6, str7, str8, str9, str10]
        f.writelines(L)

def write_rank(fname, bravais, unitcell, population):
    if not fname.endswith(".txt"):
        fname += ".txt" 
    with open(fname,"a+") as f:
        # lattice_type centering unique_axis a b c al be ga population
        for i in range(3):
           f.write(bravais[i]+" ")
        for i in range(6):
           f.write(str(float("{:.2f}".format(unitcell[i])))+" ")
        f.write(str(population)+"\n")

# Enter CELL and SYMM in create-mtz
def write_createMtz(expName, unique_unitcell, spacegroup, fname):
    cmd="""#!/bin/sh
OUTFILE=`echo $1 | sed -e 's/\.hkl$/.mtz/'`

echo " Input: $1"
echo "Output: $OUTFILE"
sed -n '/End\ of\ reflections/q;p' $1 > create-mtz.temp.hkl

echo "Running 'f2mtz'..."
f2mtz HKLIN create-mtz.temp.hkl HKLOUT $OUTFILE > out.html << EOF
TITLE Reflections from CrystFEL
NAME PROJECT wibble CRYSTAL wibble DATASET wibble
CELL %.2f %.2f %.2f %.2f %.2f %.2f
SYMM %s
SKIP 3
LABOUT H K L IMEAN SIGIMEAN
CTYPE  H H H J     Q
FORMAT '(3(F4.0,1X),F10.2,10X,F10.2)'
EOF

if [ $? -ne 0 ]; then echo "Failed."; exit; fi

rm -f create-mtz.temp.hkl
echo "Done."
""" % (unique_unitcell[0], unique_unitcell[1], unique_unitcell[2], \
unique_unitcell[3], unique_unitcell[4], unique_unitcell[5], spacegroup)
    with open(fname,"w") as f:
        f.write(cmd)
    os.chmod(fname, stat.S_IRWXU | stat.S_IRGRP | stat.S_IROTH)
    print "Prepared: ", fname

numIndex, numHits, indexHistogram, bravais = ei.getIndexHistogram(streamfile)
lattice = indexHistogram[:,9:15].copy() 

## Look at distribution over all centering types
myUC=["a","b","c","al","be","ga"]
cen_types = list(set(bravais[1]));
cen_ind = collections.defaultdict(list)
for i in cen_types:
    cen_ind[i] = []
for i, val in enumerate(bravais[1]):
    cen_ind[val].append(i)

for cen in cen_types:
    print "*** Trying centering: ", cen
    lattice_cen = lattice[cen_ind[cen]]
    lattice_type = [bravais[0][k] for k in cen_ind[cen]]
    unique_axis = [bravais[2][k] for k in cen_ind[cen]]

    uc=collections.defaultdict(list)
    for i in range(len(myUC)):
        print "max: ", np.max(lattice_cen[:,i])
        hist,bin_edges=np.histogram(lattice_cen[:,i],bins=np.arange(0,np.max(lattice_cen[:,i]),binSize))
        uc[myUC[i]].append(hist)

    ## 1D histogram peak finding
    foundPeaks = True
    possible = []
    win=signal.hann(15)
    for j in range(3):
        conv=signal.convolve(uc[myUC[j]][0],win,mode='same')/sum(win)
        peakind = signal.find_peaks(uc[myUC[j]][0], prominence=10, distance=15)
        if doPlot:
            plt.subplot(211); plt.plot(uc[myUC[j]][0],'b-'); plt.title(myUC[j])
            plt.subplot(212); plt.plot(conv,'g-'); plt.plot(peakind[0],conv[peakind[0]],'ro'); plt.title("conv and peaks found"); plt.show()
        if len(peakind[0]) == 0:
            print "Unable to find peak in unitcell "+myUC[j]+" for "+cen+". Try again after indexing more data."
            foundPeaks = False
        possible.append(np.array([p*binSize for p in peakind[0]]))
    print "possible uc values: ", possible
    if not foundPeaks:
        continue

    # Select lattices that appear at the possible peaks 
    ind = []
    for i, latt in enumerate(lattice_cen):
        if np.min(np.abs(possible[0]-latt[0])) < atol and \
           np.min(np.abs(possible[1]-latt[1])) < atol and \
           np.min(np.abs(possible[2]-latt[2])) < atol:
            ind.append(i)  

    sublatt = lattice_cen[ind,:]
    sublattice_type = [lattice_type[x] for x in ind]
    subunique_axis = [unique_axis[x] for x in ind]

    # K-means clustering
    topK = np.max([len(x) for x in possible])
    kmeans = KMeans(n_clusters=topK, random_state=0).fit(sublatt)
    print "kmeans: ", kmeans.cluster_centers_

    # Plot softmax based on cluster size
    score = np.zeros(topK,)
    for i in range(topK):
        score[i] = len(np.where(kmeans.labels_==i)[0])   

    score_norm = score / np.max(score) # normalize
    soft=np.exp(score_norm)/np.sum(np.exp(score_norm)) # softmax
    candidates = np.where(soft>=1./topK)[0] # choose ones with higher than 1/topK probability
    idx = np.argsort(soft[candidates])[::-1] # highest -> lowest prob
    if doPlot: plt.plot(soft, 'bx'); plt.plot(candidates,soft[candidates],'ro'); plt.title("softmax unitcell probability"); plt.show()
    for i in range(topK):
        print i, ": unitcell=", kmeans.cluster_centers_[i], ", Prob=", soft[i]

    # Write unitcell candidates for each centering
    unique_unitcell = []
    with open(expName+"_"+cen+"_unitcell_candidates.txt","w") as f:
        f.write("# a b c al be ga probability population *:candidate\n")
        for i in range(topK):
            for x in kmeans.cluster_centers_[i]: # unitcell_candidates.txt file
                _u = '%.2f' % x
                f.write(_u+" ")
            _u = '%.2f' % soft[i]
            f.write(_u+" ")
            _u = '%d' % score[i]
            f.write(_u)
            if i in candidates: 
                f.write("*\n")
            else:
                f.write("\n")
            unique_unitcell.append(kmeans.cluster_centers_[i])
    print "unique uc: ", unique_unitcell

    probable_centers = np.zeros((len(idx),6))
    for i, val in enumerate(idx):
        c = candidates[val]
        print i, ": unitcell=", kmeans.cluster_centers_[c], ", Prob=", soft[c]
        probable_centers[i,:] = kmeans.cluster_centers_[c]

    # remove similar unitcells
    rm_list = []
    for i in range(len(idx)):
        for j in range(len(idx)):
            remove = True
            if i < j:
                print "comparing: ",i,j, probable_centers[i,:], probable_centers[j,:]
                for k in np.arange(3):
                    print "val: ", probable_centers[i,k],probable_centers[j,k]
                    if not np.isclose(probable_centers[i,k],probable_centers[j,k],atol=atol):
                        print "Different unitcell axis. Move on to next one"
                        remove = False
                for k in np.arange(3,6):
                    print "val: ", probable_centers[i,k],probable_centers[j,k]
                    if not np.isclose(probable_centers[i,k],probable_centers[j,k],atol=atol):# and \
#                       not np.isclose(probable_centers[i,k],np.abs(180-probable_centers[j,k]),atol=atol):
                        print "*Different unitcell angle. Move on to next one"
                        remove = False
                if remove:
                    print "Similar unitcell. Remove this one"
                    rm_list.append(j)

    # Write unitcell_candidates and .cell files and create-mtz files
    num_candidates = 0
    createMtzList = []
    for i, val in enumerate(idx):
        c = candidates[val]
        if not i in rm_list:
            # figure out what Bravais lattice to use
            _ind = np.where(kmeans.labels_==c)[0]
            _latt_type = [sublattice_type[x] for x in _ind]
            _uniq_axis = [subunique_axis[x] for x in _ind]
            _set_latt = list(set(_latt_type))
            _set_axis = list(set(_uniq_axis))
            _latt_count = [_latt_type.count(x) for x in _set_latt]
            _axis_count = [_uniq_axis.count(x) for x in _set_axis]
            probable_latt_type = _set_latt[np.argmax(_latt_count)]
            probable_uniq_axis = _set_axis[np.argmax(_axis_count)]
            _cname = expName+"-"+probable_latt_type[:4]+cen+str(num_candidates)
            write_cell(_cname, (probable_latt_type,cen,probable_uniq_axis), probable_centers[i,:])
 # write .cell file
            write_rank(rankName, (probable_latt_type,cen,probable_uniq_axis), probable_centers[i,:], np.max(_latt_count))
            sg = probable_latt_type + "_" + cen
            _fname = "create-mtz"+"-"+_cname
            write_createMtz(expName, probable_centers[i,:], spacegroup_guess[sg], _fname) # write create-mtz file
            createMtzList.append(_fname)
            num_candidates += 1

# Rank the unitcells of possible Bravais lattices
population = []
with open(expName+"_unitcell_rank.txt","w") as g:
    for cen in cen_types:
        _fname = expName+"_"+cen+"_unitcell_candidates.txt"
        if os.path.exists(_fname):
            with open(_fname,"r") as f:
                lines = f.readlines()
            for i,val in enumerate(lines):
                if val.endswith("*\n"): # candidate
                    g.write(cen+str(i)+": "+val.split("*")[0]+"\n")
                    population.append(int(val.split()[-1].split("*")[0]))

# rank higher symmetries as more favorable
population = []
recommend = []
with open(expName+"_rank.txt") as f:
    lines = f.readlines()
    for i,val in enumerate(lines):
        recommend.append(val.split()[0])
        population.append(int(val.split()[-1]))

population = np.array(population)
population_norm = population / np.max(population) # normalize
soft_pop=np.exp(population_norm)/np.sum(np.exp(population_norm)) # softmax
idx_pop = np.argsort(soft_pop)[::-1] # highest -> lowest prob
print "Most likely unitcell is: %s %.2f%%" %(recommend[idx_pop[0]], soft_pop[idx]*100)
