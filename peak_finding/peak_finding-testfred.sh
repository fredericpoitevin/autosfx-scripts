#!/bin/bash
#prevent crash when running on one core
export HDF5_USE_FILE_LOCKING=FALSE

# activate psana environment
source /img/conda.local/env.local
source activate psana_base

# set location for experiment db and calib dir
export SIT_DATA=$CONDA_PREFIX/data
export SIT_PSDM_DATA=/global/cscratch1/sd/psdatmgr/data/psdm

#PSOCAKE
export PATH=/project/projectdirs/lcls/SFX_automation/psocake/app:$PATH
export PYTHONPATH=/project/projectdirs/lcls/SFX_automation/psocake:$PYTHONPATH
export PSOCAKE_FACILITY=LCLS
peakfinder="findPeaksCori1"

#============#
# PARAMETERS #
#============#

EXPERIMENT_NAME=$1
RUN_NUM=$2
DETECTOR=$3
MASK="/project/projectdirs/lcls/SFX_automation/peak_finding/staticMask.h5"
INSTRUMENT=${EXPERIMENT_NAME:0:3}
CLEN="CXI:DS2:MMS:06.RBV"
TAG=$4

# define output directory
printf -v run "%04d" $RUN_NUM
outdir="${SIT_PSDM_DATA}/${instrument}/${EXPERIMENT_NAME}/scratch/r${run}/peak-finding/"

if [ ! -d $outdir ]; then
  mkdir -p -m777 $outdir
fi

#=====#
# JOB #
#=====#

$peakfinder \
  --exp $EXPERIMENT_NAME \
  --run $RUN_NUM \
  --det $DETECTOR \
  --outDir $outdir \
  --algorithm 2 \
  --alg_npix_min 2.0 \
  --alg_npix_max 30.0 \
  --alg_amax_thr 300.0 \
  --alg_atot_thr 600.0 \
  --alg_son_min 10.0 \
  --alg1_thr_low 0.0 \
  --alg1_thr_high 0.0 \
  --alg1_rank 3 \
  --alg1_radius 3 \
  --alg1_dr 2 \
  --psanaMask_on True \
  --psanaMask_calib True \
  --psanaMask_status True \
  --psanaMask_edges True \
  --psanaMask_central True \
  --psanaMask_unbond True \
  --psanaMask_unbondnrs True \
  --mask $MASK \
  --sample sample \
  --instrument $INSTRUMENT \
  --clen $CLEN \
  --coffset 0.3189938 \
  --detectorDistance 0.144 \
  --pixelSize 0.00010992 \
  --minPeaks 15 \
  --maxPeaks 2048 \
  --minRes -1 \
  --auto False \
  --access ana \
  --tag $TAG

RC=$?
exit $RC
