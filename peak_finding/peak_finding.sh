#!/bin/bash


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

#prevent crash when running on one core
export HDF5_USE_FILE_LOCKING=FALSE

#outdir=/global/cscratch1/sd/psdatmgr/reg/d/psdm/cxi/cxic0515/scratch
outdir=/global/cscratch1/sd/chuck

findPeaks -e cxic0515 -d CxiDs2.0:Cspad.0 --outDir $outdir/r0081 --algorithm 2 --alg_npix_min 2.0 --alg_npix_max 30.0 --alg_amax_thr 300.0 --alg_atot_thr 600.0 --alg_son_min 10.0 --alg1_thr_low 0.0 --alg1_thr_high 0.0 --alg1_rank 3 --alg1_radius 3 --alg1_dr 2 --psanaMask_on True --psanaMask_calib True --psanaMask_status True --psanaMask_edges True --psanaMask_central True --psanaMask_unbond True --psanaMask_unbondnrs True --mask $outdir/r0081/staticMask.h5 --clen CXI:DS2:MMS:06.RBV --coffset 0.3189938 --minPeaks 15 --maxPeaks 2048 --minRes -1 --sample sample --instrument CXI --pixelSize 0.00010992 --auto False --detectorDistance 0.144 --access ana -r 81
