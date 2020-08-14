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

# ccp4
source /img/ccp4-7.1/bin/ccp4.setup-sh

#prevent crash when running on one core
export HDF5_USE_FILE_LOCKING=FALSE

indexCrystals -e cxic0515 -d CxiDs2.0:Cspad.0 --geom $SCRATCH/r0081/.temp.geom --peakMethod cxi --integrationRadius 3,4,5 --indexingMethod mosflm --minPeaks 15 --maxPeaks 2048 --minRes -1 --tolerance 5,5,5,1.5 --outDir $SCRATCH --sample crystal --queue psanaq --chunkSize 10 --noe -1 --instrument CXI --pixelSize 0.00010992 --coffset 0.3189936 --clenEpics CXI:DS2:MMS:06.RBV --logger False --hitParam_threshold 15 --keepData True -v 0 --run 81 > temp.log

