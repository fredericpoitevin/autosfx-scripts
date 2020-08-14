#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-phasing-summary
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=00:20:00
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
nersc_summary=${nersc_scratch}'summary'

echo "SCRATCH work directory: $nersc_scratch"

#==================#
# Job requirements #
#==================#
# - this is the phasing summary task:
#   check that executable is found
execdir=${nersc_srcdir}phasing/sfxPhasing/sfxPhasing/
if [ ! -d $execdir ]; then
  echo "Abort! could not find $execdir"
  echo "Steps to follow at $PWD:"
  echo "$> git clone git@github.com:slac-lcls/sfxPhasing.git"
  echo "$> cd sfxPhasing"
  echo "$> checkout -t origin/cori" 
  exit
fi
#   check 'summary' directory exists
if [ ! -d ${nersc_scratch}summary/ ]; then
  mkdir -p -m777 ${nersc_scratch}summary/
fi 
#   check that final results file exists
if [ ! -f ${nersc_scratch}reconstruction/final_result.txt ]; then
  echo "Abort! could not find ${nersc_scratch}reconstruction/final_result.txt"
fi

cd ${nersc_scratch}summary
echo "Current work directory: $PWD"
rm -f heatmaps.py
ln -sf $execdir/heatmaps.py .

#==============#
# Job Launcher #
#==============#

copy_list=`cat ${nersc_scratch}reconstruction/final_result.txt | awk '{print $1}' | awk -v FS='_' '{print$2}' | sort -u`

echo $copy_list
for copy in $copy_list; do
  echo "#  srun -n 1 shifter python heatmaps.py -f ${nersc_scratch}reconstruction/final_result.txt -k $copy -d 'prob'"
done
#for copy in $copy_list; do
#  srun -n 1 shifter python heatmaps.py -f ${nersc_scratch}reconstruction/final_result.txt \
#	             -k $copy \
#		     -d 'prob'
#  srun -n 1 shifter python heatmaps.py -f ${nersc_scratch}reconstruction/final_result.txt \
#                     -k $copy \
#                     -d 'TFZ'
#done	           




