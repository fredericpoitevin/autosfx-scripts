#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-reconstruction-merging
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=02:00:00
#SBATCH --image=docker:slaclcls/autosfx:latest
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
# - this is the merging task:
#   check that 'merging/stream2mtz.sh' is found
if [ ! -f ${nersc_srcdir}merging/stream2mtz.sh ]; then
  echo "Abort: could not find ${nersc_srcdir}merging/stream2mtz.sh"
  exit
fi
# - merging task is part of reconstruction workflow
#   check 'reconstruction' directory exists
if [ ! -d ${nersc_scratch}reconstruction ]; then
  mkdir -p -m777 ${nersc_scratch}reconstruction
fi 
# <!-- temporary fix
#if [ ! -d ${nersc_scratch}consensus ]; then
#  mkdir -p -m777 ${nersc_scratch}consensus
#  cp /global/cfs/cdirs/lcls/exp/cxi/cxic0515/scratch/old/cxic0415.stream \
#     "${nersc_scratch}consensus/final.stream"
#cp /global/cfs/cdirs/lcls/exp/cxi/cxic0515/scratch/old/strep_more.cell \
#     "${nersc_scratch}consensus/final.cell"
#fi
# -->
# - reconstruction workflow follows consensus workflow
#   check 'consensus' directory and contains the following files:
#   - final.cell
#   - final.stream
for file in cell stream; do
  if [ ! -f "${nersc_scratch}consensus/final.${file}" ]; then
    echo "Abort: could not find ${nersc_scratch}consensus/final.${file}"
    exit
  fi
done

# TODO: user-defined parameters


#==============#
# Job Launcher #
#==============#
srun -n 1 -c 1 shifter \
    "${nersc_srcdir}merging/stream2mtz.sh"  \
      stream:"${nersc_scratch}consensus/final.stream"  \
      jobname:"merging"  \
      ucell:"${nersc_scratch}consensus/final.cell" \
      pgroup:2  \
      sgnum:4  \
      maxadu:13500  \
      wavela:0.969  \
      merge:TRUE  \
      friedel:FALSE  \
      workdir:"${nersc_scratch}reconstruction/" \
      highres:1.5

