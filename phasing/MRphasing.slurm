#!/usr/bin/env bash
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-reconstruction-MR-phasing
#SBATCH --nodes=20
#SBATCH --tasks-per-node=20
#SBATCH --constraint=haswell
#SBATCH --time=04:00:00
#SBATCH --image=docker:registry.services.nersc.gov/annagian/sfx_6
#SBATCH --gres=craynetwork:4
#SBATCH --qos=realtime

echo "Batch script directory: $PWD"

#=====================#
# Workflow management #
#=====================#
nersc_rootdir='/global/cscratch1/sd/psdatmgr/data/psdm/'
nersc_srcdir='/global/project/projectdirs/lcls/SFX_automation/'

config_file=$nersc_srcdir'current_analysis.config'
if [ ! -f $config_file ]; then
  echo "Abort: missing $config_file"
  exit
fi


#=======================#
# Experiment management #
#=======================#
experiment=`<$config_file`
instrument=${experiment:0:3}

nersc_expdir=${nersc_rootdir}${instrument}'/'${experiment}'/'
nersc_scratch=${nersc_expdir}'scratch/fred/'

echo "SCRATCH work directory: $nersc_scratch"

#==================#
# Job requirements #
#==================#
# - this is the phasing task:
#   check that executable is found
execdir=${nersc_srcdir}phasing/sfxPhasing/sfxPhasing/MR_phasing/
if [ ! -d $execdir ]; then
  echo "Abort! could not find $execdir"
  echo "Steps to follow at $PWD:"
  echo "$> git clone git@github.com:slac-lcls/sfxPhasing.git"
  echo "$> cd sfxPhasing"
  echo "$> checkout -t origin/cori" 
  exit
#else
#  export PATH=${nersc_srcdir}phasing/sfxPhasing/sfxPhasing/MR_phasing/:$PATH
#  echo $PATH
#  for exe in MR_batch.py MR_pip.py; do
#    if ! command -v $exe $> /dev/null; then
#      echo "Abort! Could not find $exe"
#      exit
#    fi
#  done
fi
# - phasing task is part of reconstruction workflow
#   check 'reconstruction' directory exists
if [ ! -d ${nersc_scratch}reconstruction ]; then
  mkdir -p -m777 ${nersc_scratch}reconstruction
fi 
#   check that the merged reflections are available
if [ ! -f ${nersc_scratch}reconstruction/merged.mtz ]; then
  # echo "Abort! could not find ${nersc_scratch}reconstruction/merged.mtz"
  # exit
  # <!-- temporary fix
  cp ${nersc_srcdir}share/GPCR/mt2_push1d2_xscale_ccp4if_Rfree.mtz \
     "${nersc_scratch}reconstruction/merged.mtz"
  # -->
fi
# - this is MR phasing workflow
#   check that sequence and initial model are available
MRmodel=${nersc_scratch}user_data/MRmodel.pdb
if [ ! -f $MRmodel ]; then
  echo "Abort! Could not find $MRmodel"
  exit
fi
MRfasta=${nersc_scratch}user_data/MR.fasta
if [ ! -f $MRfasta ]; then
  echo "Abort! Could not find $MRfasta"
  exit
fi
# - not ideal, but let's link the python script to the work directory
cd ${nersc_scratch}reconstruction
echo "Current work directory: $PWD"
rm -f *.py
ln -sf $execdir/*.py .
# - not ideal, let's delete previous attempts if any
rm -rf ${nersc_scratch}reconstruction/Request_*_copy
rm -rf ${nersc_scratch}reconstruction/FILE_SETUP.json
rm -rf ${nersc_scratch}reconstruction/logfile.log
rm -rf ${nersc_scratch}reconstruction/final_result.txt

#==============#
# Job Launcher #
#==============#
python MR_batch.py \
  -rfl "${nersc_scratch}reconstruction/merged.mtz" \
  -pdb "$MRmodel" \
  -seq "$MRfasta" \
  -n 1 \
  --shifter 1

