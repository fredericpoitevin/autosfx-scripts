import json, h5py, os, time
import argparse
import subprocess
import numpy as np
import glob
import getpass

if 'PSOCAKE_FACILITY' not in os.environ: os.environ['PSOCAKE_FACILITY'] = 'LCLS' # Default facility
parser = argparse.ArgumentParser()
parser.add_argument('expRun', nargs='?', default=None, help="Psana-style experiment/run string in the format (e.g. exp=cxi06216:run=22). This option trumps -e and -r options.")
parser.add_argument("-e","--exp", help="Experiment name (e.g. cxis0813 ). This option is ignored if expRun option is used.", default="", type=str)
parser.add_argument("-r","--run", help="Run number. This option is ignored if expRun option is used.",default=0, type=int)
parser.add_argument("-d","--det", help="Detector alias or DAQ name (e.g. DscCsPad or CxiDs1.0:Cspad.0), default=''",default="", type=str)
parser.add_argument("--geom", help="",default="", type=str)
parser.add_argument("--peakMethod", help="",default="", type=str)
parser.add_argument("--integrationRadius", help="",default="", type=str)
parser.add_argument("--pdb", help="",default="", type=str)
parser.add_argument("--indexingMethod", help="",default="", type=str)
parser.add_argument("--tolerance", help="",default="5,5,5,1.5", type=str)
parser.add_argument("--extra", help="",default="", type=str)
parser.add_argument("--minPeaks", help="",default=0, type=int)
parser.add_argument("--maxPeaks", help="",default=0, type=int)
parser.add_argument("--minRes", help="",default=0, type=int)
parser.add_argument("-o","--outDir", help="Use this directory for output instead.", default=None, type=str)
parser.add_argument("--sample", help="", default=None, type=str)
parser.add_argument("--pkTag", help="", default='', type=str)
parser.add_argument("--tag", help="", default='', type=str)
parser.add_argument("--queue", help="", default=None, type=str)
parser.add_argument("--chunkSize", help="", default=500, type=int)
parser.add_argument("--cpu", help="", default=12, type=int)
parser.add_argument("--noe", help="", default=-1, type=int)
parser.add_argument("--instrument", help="", default=None, type=str)
parser.add_argument("--pixelSize", help="", default=0, type=float)
parser.add_argument("--coffset", help="", default=0, type=float)
parser.add_argument("--clenEpics", help="", default=None, type=str)
parser.add_argument("--logger", help="", default=False, type=bool)
parser.add_argument("--hitParam_threshold", help="", default=0, type=int)
parser.add_argument("--keepData", help="", default=False, type=str)
parser.add_argument("-v", help="verbosity level, default=0",default=0, type=int)
parser.add_argument("--likelihood", help="index hits with likelihood higher than this value", default=0, type=float)
parser.add_argument("--condition", help="logic condition", default='', type=str)
# PAL specific
parser.add_argument("--dir", help="PAL directory where the detector images (hdf5) are stored", default=None, type=str)
args = parser.parse_args()

if 'LCLS' in os.environ['PSOCAKE_FACILITY'].upper():
    facility = 'LCLS'
    #import psanaWhisperer, psana
elif 'PAL' in os.environ['PSOCAKE_FACILITY'].upper():
    facility = 'PAL'

def str2bool(v): return v.lower() in ("yes", "true", "t", "1")

username = getpass.getuser()

# Init experiment parameters
if args.expRun is not None and ':run=' in args.expRun:
    experimentName = args.expRun.split('exp=')[-1].split(':')[0]
    runNumber = int(args.expRun.split('run=')[-1])
else:
    experimentName = args.exp
    runNumber = int(args.run)
detInfo = args.det
geom = args.geom
peakMethod = args.peakMethod
integrationRadius = args.integrationRadius
pdb = args.pdb
indexingMethod = args.indexingMethod
minPeaks = args.minPeaks
maxPeaks = args.maxPeaks
minRes = args.minRes
tolerance = args.tolerance
extra = args.extra.split("[")[-1].split("]")[0].replace(","," ")
outDir = args.outDir
sample = args.sample
tag = args.tag
queue = args.queue
chunkSize = args.chunkSize
cpu = args.cpu
noe = args.noe
instrument = args.instrument
pixelSize = args.pixelSize
coffset = args.coffset
clenEpics = args.clenEpics
logger = args.logger
hitParam_threshold = args.hitParam_threshold
keepData = str2bool(args.keepData)
dir = args.dir

def checkJobExit(jobID):
    if facility == 'LCLS':
        cmd = "bjobs -d | grep " + str(jobID)
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out, err = process.communicate()
        if "EXIT" in out:
            "*********** NODE FAILURE ************ ", jobID
            return 1
        else:
            return 0
    elif facility == 'PAL':
        print "checkJobExit not implemented for PAL"

def getMyChunkSize(numJobs, numWorkers, chunkSize, rank):
    """Returns number of events assigned to the slave calling this function."""
    assert(numJobs >= numWorkers)
    allJobs = np.arange(numJobs)
    startInd = (np.arange(numWorkers)) * chunkSize
    endInd = (np.arange(numWorkers) + 1) * chunkSize
    endInd[-1] = numJobs
    myJobs = allJobs[startInd[rank]:endInd[rank]]
    return myJobs

def writeStatus(fname, d):
    json.dump(d, open(fname, 'w'))

def findPsanaGeometry():
    try:
        source = Detector.PyDetector.map_alias_to_source(self.parent.detInfo,
                                                              self.parent.exp.ds.env())  # 'DetInfo(CxiDs2.0:Cspad.0)'
        self.calibSource = self.source.split('(')[-1].split(')')[0]  # 'CxiDs2.0:Cspad.0'
        self.detectorType = gu.det_type_from_source(self.source)  # 1
        self.calibGroup = gu.dic_det_type_to_calib_group[self.detectorType]  # 'CsPad::CalibV1'
        self.detectorName = gu.dic_det_type_to_name[self.detectorType].upper()  # 'CSPAD'

        if self.parent.args.localCalib:
            self.calibPath = "./calib/" + self.calibGroup + "/" + self.calibSource + "/geometry"
        else:
            self.calibPath = self.parent.dir + '/' + self.parent.experimentName[:3] + '/' + \
                             self.parent.experimentName + "/calib/" + self.calibGroup + '/' + \
                             self.calibSource + "/geometry"
        if self.parent.args.v >= 1: print "### calibPath: ", self.calibPath

        # Determine which calib file to use
        geometryFiles = os.listdir(self.calibPath)
        if self.parent.args.v >= 1: print "geom: ", geometryFiles
        self.calibFile = None
        minDiff = -1e6
        for fname in geometryFiles:
            if fname.endswith('.data'):
                endValid = False
                try:
                    startNum = int(fname.split('-')[0])
                except:
                    continue
                endNum = fname.split('-')[-1].split('.data')[0]
                diff = startNum - self.parent.runNumber
                # Make sure it's end number is valid too
                if 'end' in endNum:
                    endValid = True
                else:
                    try:
                        if self.parent.runNumber <= int(endNum):
                            endValid = True
                    except:
                        continue
                if diff <= 0 and diff > minDiff and endValid is True:
                    minDiff = diff
                    self.calibFile = fname
    except:
        if self.parent.args.v >= 1: print "Couldn't find psana geometry"
        self.calibFile = None

def deployCrystfelGeometry(arg):
    self.findPsanaGeometry()
    if self.calibFile is not None and self.parent.writeAccess:
        # Convert psana geometry to crystfel geom
        if '.temp.geom' in self.parent.index.geom:
            self.parent.index.p9.param(self.parent.index.index_grp,
                                       self.parent.index.index_geom_str).setValue(
                self.parent.psocakeRunDir + '/.temp.geom')
            cmd = ["psana2crystfel", self.calibPath + '/' + self.calibFile,
                   self.parent.psocakeRunDir + "/.temp.geom", str(self.parent.coffset)]
            if self.parent.args.v >= 1: print "cmd: ", cmd
            try:
                p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
                p.communicate()[0]
                p.stdout.close()
            except:
                print highlight("Warning! deployCrystfelGeometry() failed.", 'r', 1)
            # FIXME: Configure crystfel geom file to read in a mask (crystfel 'mask_file=' broken?)
            with open(self.parent.psocakeRunDir + '/.temp.geom', 'r') as f: lines = f.readlines()
            newGeom = []
            for line in lines:
                if '; mask =' in line:
                    newGeom.append(line.split('; ')[-1])
                elif '; mask_good =' in line:
                    newGeom.append(line.split('; ')[-1])
                elif '; mask_bad =' in line:
                    newGeom.append(line.split('; ')[-1])
                elif '; clen =' in line:
                    newGeom.append(line.split('; ')[-1])
                elif '; photon_energy =' in line:
                    newGeom.append(line.split('; ')[-1])
                elif '; adu_per_eV =' in line:
                    if 'epix10k' in self.parent.detInfo.lower() or \
                       'jungfrau4m' in self.parent.detInfo.lower():
                        newGeom.append(line.split('; ')[-1].split('0.1')[0]+"0.001")
                    else:
                        newGeom.append(line.split('; ')[-1])
                else:
                    newGeom.append(line)
            with open(self.parent.psocakeRunDir + '/.temp.geom', 'w') as f: lines = f.writelines(newGeom)

def getIndexedPeaks():
    # Merge all stream files into one
    if not tag:
        totalStream = runDir + "/" + experimentName + "_" + str(runNumber).zfill(4) + ".stream"
    else:
        totalStream = runDir + "/" + experimentName + "_" + str(runNumber).zfill(4) + "_" + tag + ".stream"
    with open(totalStream, 'w') as outfile:
        for fname in myStreamList:
            try:
                with open(fname) as infile:
                    outfile.write(infile.read())
            except:  # file may not exist yet
                pass

    # Add indexed peaks and remove images in hdf5
    try:
        f = h5py.File(peakFile, 'r')
        totalEvents = len(f['/entry_1/result_1/nPeaksAll'])
        if facility == 'LCLS':
            hitEvents = f['/LCLS/eventNumber'][()]
        elif facility == 'PAL':
            hitEvents = f['/PAL/eventNumber'][()]
        f.close()
        # Add indexed peaks
        fstream = open(totalStream, 'r')
        content = fstream.readlines()
        fstream.close()
        indexedPeaks = -1 * np.ones((totalEvents,), dtype=int)
        numProcessed = 0
        for i, val in enumerate(content):
            if "Event: //" in val:
                _evt = int(val.split("Event: //")[-1].strip())
            if "indexed_by =" in val:
                _ind = val.split("indexed_by =")[-1].strip()
            if "fs/px" in val:
                startPeak = i
            if "End of peak list" in val:
                numPeaks = i - startPeak - 1
                numProcessed += 1
                if 'none' in _ind:
                    indexedPeaks[hitEvents[_evt]] = 0
                else:
                    indexedPeaks[hitEvents[_evt]] = numPeaks
        try:
            f = h5py.File(peakFile, 'r+')
            if '/entry_1/result_1/index' in f: del f['/entry_1/result_1/index']
            f['/entry_1/result_1/index'] = indexedPeaks
            f.close()
        except:
            pass
    except:
        indexedPeaks = None
        numProcessed = None
    return indexedPeaks, numProcessed
##############################################################################
runDir = outDir + "/r" + str(runNumber).zfill(4)
peakFile = runDir + '/' + experimentName + '_' + str(runNumber).zfill(4)
if args.pkTag: peakFile += '_'+args.pkTag
peakFile += '.cxi'
fnameIndex = runDir+"/status_index"
if args.pkTag: fnameIndex += '_'+args.pkTag
fnameIndex += ".txt"





#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
def getpath(cxi_name):
    global search_name, hf
    if cxi_name.endswith(search_name):
        try: hf[cxi_name][()]
        except Exception: return None
        return cxi_name

def condition_check(hf, ival, iicondition):
    if not iicondition: return True
    exec('itest = ' + iicondition)
    if itest: return True
    return False

hf = h5py.File(peakFile, 'r')
icondition = args.condition
iposition = [ipos for ipos, ichar in enumerate(icondition) if ichar == '#']
print '##################'
print 'original condition = ', icondition
istart = iposition[0::2]
iend = iposition[1::2]
assert (len(istart) == len(iend))
iname = [icondition[(istart[i]+1):iend[i]] for i in range(len(istart))]
ifullpath = []
for idx in range(len(istart)): 
    search_name = iname[idx]
    assert(hf.visit(getpath))
    ifullpath.append("hf['"+hf.visit(getpath)+"'][ival]")
    icondition = icondition.replace('#'+iname[idx]+'#', ifullpath[-1])
print 'modified condition = ', icondition, '\n'
print '##################'
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

try:
    if facility == 'LCLS':
        f = h5py.File(peakFile, 'r')
        hasData = '/entry_1/instrument_1/detector_1/data' in f and f['/status/findPeaks'][()] == 'success'
        minPeaksUsed = f["entry_1/result_1/nPeaks"].attrs['minPeaks']
        maxPeaksUsed = f["entry_1/result_1/nPeaks"].attrs['maxPeaks']
        minResUsed = f["entry_1/result_1/nPeaks"].attrs['minRes']
        f.close()
except:
    print "Error while reading: ", peakFile
    print "Note that peak finding has to finish before launching indexing jobs"
    exit()

if hasData:
    # Update elog
    if logger == True:
        if args.v >= 1: print "Start indexing"
        try:
            d = {"message": "#StartIndexing"}
            writeStatus(fnameIndex, d)
        except:
            pass
    # Launch indexing
    try:
        if facility == 'LCLS':
            print "Reading images from: ", peakFile
            f = h5py.File(peakFile, 'r')
            eventList = f['/LCLS/eventNumber'][()]
            if args.likelihood > 0:
                likelihood = f['/entry_1/result_1/likelihood'][()]
            numEvents = len(eventList)
            f.close()
        elif facility == 'PAL':
            f = h5py.File(peakFile, 'r')
            eventList = f['/PAL/eventNumber'][()]
            numEvents = len(eventList)
            f.close()
    except:
        print "Couldn't read file: ", peakFile

    if facility == 'LCLS':
        # Split into chunks for faster indexing
        numWorkers = int(np.ceil(numEvents*1./chunkSize))
        print "numWorkers: ", numWorkers, numEvents, chunkSize
        myLogList = []
        myJobList = []
        myStreamList = []
        myLists = []
        for rank in range(numWorkers):
            myJobs = getMyChunkSize(numEvents, numWorkers, chunkSize, rank)
            if tag is '':
                jobName = experimentName + "_" + str(runNumber) + "_" + str(rank)
            else:
                jobName = experimentName + "_" + str(runNumber) + "_" + str(rank) + "_" + tag
            myList = runDir + "/temp_" + jobName + ".lst"
            myStream = runDir + "/temp_" + jobName + ".stream"
            myStreamList.append(myStream)
            myLists.append(myList)

            # Write list
            isat_event = []
            checkEnoughLikes = 0
            with open(myList, "w") as text_file:
                for i, val in enumerate(myJobs):
                    if args.likelihood > 0:
                        if likelihood[val] >= args.likelihood and condition_check(hf, val, icondition):
                            text_file.write("{} //{}\n".format(peakFile, val))
                            checkEnoughLikes += 1
                            isat_event.append(val)
                    else:
                        if condition_check(hf, val, icondition):
                            text_file.write("{} //{}\n".format(peakFile, val))
                            isat_event.append(val)
            print 'satisfied event: ', isat_event, '\n'
            isat_event = []

            # Submit job
            print "rank: ", rank
            #cmd = "bsub -q " + queue + " -o " + runDir + "/.%J.log -J " + jobName + " -n 1 -x"
            coreNumber = 6
            _log = runDir + "/" + str(os.getpid())+'_'+str(rank)+'.log'
            myLogList.append(_log)
            cmd = 'srun -n 1 --mem=5000 --gres=craynetwork:0 --cpus-per-task='+str(coreNumber)+' -o '+_log+' shifter /img/load_everything.sh '
            cmd += "indexamajig -i " + myList
            if args.likelihood > 0 and checkEnoughLikes > 0 and checkEnoughLikes <= coreNumber:
                cmd += " -j 1"
            else:
                cmd += " -j "+str(coreNumber)
            cmd += " -g " + geom + " --peaks=" + peakMethod + " --int-radius=" + integrationRadius + \
                   " --indexing=" + indexingMethod + " -o " + myStream + \
                   " --temp-dir=" + runDir + \
                   " --tolerance=" + tolerance + \
                   " --no-revalidate --profile"
            if pdb: cmd += " --pdb=" + pdb
            if extra: cmd += " " + extra

            print "Submitting job: ", cmd
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
            #myLogList.append(%J.log)
            time.sleep(1)
            print "Popen: ", rank, process, process.pid, process.returncode, os.getpid()
            #
            #out, err = process.communicate()

            # Keep list
            #print "out: ", out
            #print "err: ", err
            #jobID = out.split("<")[1].split(">")[0]
            #myLog = runDir + "/." + jobID + ".log"
            #myJobList.append(jobID)
            #myLogList.append(myLog)
            #print "bsub log filename: ", myLog

    ################
    # Wait for all indexing jobs to finish
    myKeyString = "Final:"
    numCrystals = 0
    numLeft = len(myLogList)
    while numLeft:
        numLeft = len(myLogList)
        numCrystals = 0
        for _log in myLogList:
            try:
                lines = open(_log).readlines()
                for line in lines:
                    if myKeyString in line:
                        numLeft -= 1
                        print "rank: ", rank, line
                        numCrystals += int(line.split("processed,")[1].split("had")[0])
                        print "@ ", line.split("processed"),line.split("had"),line.split("processed,")[1].split("had")[0] 
                       #Final: 10 images processed, 6 had crystals (60.0%), 6 crystals overall.
            except:
                pass
            time.sleep(5)
    print "All done: ", numCrystals

    numHits = 0
    try:
        f = h5py.File(peakFile, 'r')
        hitEvents = f['/entry_1/result_1/nPeaksAll'][()]
        numHits = len(np.where(hitEvents >= hitParam_threshold)[0])
        f.close()
    except:
        print "Couldn't read: ", peakFile

    # Merge all stream files into one
    indexedPeaks, numProcessed = getIndexedPeaks()
    if indexedPeaks is not None:
        numIndexedNow = len(np.where(indexedPeaks > 0)[0])
        if numProcessed == 0:
            indexRate = 0
        else:
            indexRate = numIndexedNow * 100. / numProcessed
        fracDone = numProcessed * 100. / numHits
        if args.v >= 1: print "Progress [runNumber, numIndexed, indexRate, fracDone]: ", runNumber, numIndexedNow, indexRate, fracDone

        try:
            d = {"numIndexed": numIndexedNow, "indexRate": indexRate, "fracDone": fracDone}
            writeStatus(fnameIndex, d)
        except:
            pass

    # Write number of indexed
    try:
        f = h5py.File(peakFile, 'r+')
        if '/entry_1/result_1/index' in f: del f['/entry_1/result_1/index']
        indexedPeaks[np.where(indexedPeaks==-1)] = -2 # This is required to indicate indexing has finished
        f['/entry_1/result_1/index'] = indexedPeaks
        # Remove large data
        if keepData == False:
            if '/entry_1/instrument_1/detector_1/data' in f:
                del f['/entry_1/instrument_1/detector_1/data']
        f.close()
    except:
        if args.v >= 0: print "Couldn't modify hdf5 file: ", peakFile
        pass

    # Clean up temp files
    for fname in myStreamList:
        os.remove(fname)
    for fname in myLists:
        os.remove(fname)

    ################
"""
    if facility == 'LCLS':
        myKeyString = "The output (if any) is above this job summary."
        mySuccessString = "Successfully completed."
        Done = 0
        haveFinished = np.zeros((numWorkers,))
        try:
            f = h5py.File(peakFile, 'r')
            hitEvents = f['/entry_1/result_1/nPeaksAll'][()]
            numHits = len(np.where(hitEvents >= hitParam_threshold)[0])
            f.close()
        except:
            print "Couldn't read file: ", peakFile
            fname = runDir + '/status_peaks.txt'
            print "Try reading file: ", fname
            with open(fname) as infile:
                d = json.load(infile)
                numEvents = int(d['numHits'])

        while Done == 0:
            for i, myLog in enumerate(myLogList):
                if os.path.isfile(myLog):  # log file exists
                    if haveFinished[i] == 0:  # job has not finished
                        p = subprocess.Popen(["grep", myKeyString, myLog], stdout=subprocess.PIPE)
                    if haveFinished[i] == 0:  # job has not finished
                        p = subprocess.Popen(["grep", myKeyString, myLog], stdout=subprocess.PIPE)
                    if haveFinished[i] == 0:  # job has not finished
                        p = subprocess.Popen(["grep", myKeyString, myLog], stdout=subprocess.PIPE)
                        output = p.communicate()[0]
                        p.stdout.close()
                        if myKeyString in output:  # job has completely finished
                            # check job was a success or a failure
                            p = subprocess.Popen(["grep", mySuccessString, myLog], stdout=subprocess.PIPE)
                            output = p.communicate()[0]
                            p.stdout.close()
                            if mySuccessString in output:  # success
                                print "successfully done indexing: ", runNumber, myLog
                                haveFinished[i] = 1
                                if len(np.where(abs(haveFinished) == 1)[0]) == numWorkers:
                                    print "Done indexing"
                                    Done = 1
                            else:  # failure
                                print "failed attempt", runNumber, myLog
                                haveFinished[i] = -1
                                if len(np.where(abs(haveFinished) == 1)[0]) == numWorkers:
                                    print "Done indexing"
                                    Done = -1
                        else:  # job is still going, update indexing rate
                            if args.v >= 1: print "indexing hasn't finished yet: ", runNumber, myJobList, haveFinished
                            indexedPeaks = None#, numProcessed = getIndexedPeaks()

                            if indexedPeaks is not None:
                                numIndexedNow = len(np.where(indexedPeaks > 0)[0])
                                if numProcessed == 0:
                                    indexRate = 0
                                else:
                                    indexRate = numIndexedNow * 100. / numProcessed
                                fracDone = numProcessed * 100. / numHits

                                if args.v >= 1: print "Progress [runNumber, numIndexed, indexRate, fracDone]: ", runNumber, numIndexedNow, indexRate, fracDone
                                try:
                                    d = {"numIndexed": numIndexedNow, "indexRate": indexRate, "fracDone": fracDone}
                                    writeStatus(fnameIndex, d)
                                except:
                                    print "Couldn't update status"
                                    pass
                            else:
                                pass #print "getIndexedPeaks returned None"
                            time.sleep(30)
                else:
                    if args.v >= 1: print "no such file yet: ", runNumber, myLog
                    nodeFailed = 0#checkJobExit(myJobList[i])
                    if nodeFailed == 1:
                        if args.v >= 0: print "indexing job node failure: ", myLog
                        haveFinished[i] = -1
                    time.sleep(10)

    if abs(Done) == 1:
        indexedPeaks, numProcessed = getIndexedPeaks()
        if indexedPeaks is not None:
            numIndexedNow = len(np.where(indexedPeaks > 0)[0])
            if numProcessed == 0:
                indexRate = 0
            else:
                indexRate = numIndexedNow * 100. / numProcessed
            fracDone = numProcessed * 100. / numHits
            if args.v >= 1: print "Progress [runNumber, numIndexed, indexRate, fracDone]: ", runNumber, numIndexedNow, indexRate, fracDone

            try:
                d = {"numIndexed": numIndexedNow, "indexRate": indexRate, "fracDone": fracDone}
                writeStatus(fnameIndex, d)
            except:
                pass

        if args.v >= 1: print "Merging stream file: ", runNumber
        # Merge all stream files into one
        if tag is '':
            totalStream = runDir + "/" + experimentName + "_" + str(runNumber).zfill(4) + ".stream"
        else:
            totalStream = runDir + "/" + experimentName + "_" + str(runNumber).zfill(4) + "_" + tag + ".stream"
        with open(totalStream, 'w') as outfile:
            for fname in myStreamList:
                with open(fname) as infile:
                    outfile.write(infile.read())

        indexedPeaks, _ = getIndexedPeaks()
        numIndexed = len(np.where(indexedPeaks > 0)[0])

        # Write number of indexed
        try:
            f = h5py.File(peakFile, 'r+')
            if '/entry_1/result_1/index' in f: del f['/entry_1/result_1/index']
            indexedPeaks[np.where(indexedPeaks==-1)] = -2 # This is required to indicate indexing has finished
            f['/entry_1/result_1/index'] = indexedPeaks
            # Remove large data
            if keepData == False:
                if '/entry_1/instrument_1/detector_1/data' in f:
                    del f['/entry_1/instrument_1/detector_1/data']
            f.close()
        except:
            if args.v >= 0: print "Couldn't modify hdf5 file: ", peakFile
            pass

        # Clean up temp files
        for fname in myStreamList:
            os.remove(fname)
        for fname in myLists:
            os.remove(fname)
"""
hf.close()
