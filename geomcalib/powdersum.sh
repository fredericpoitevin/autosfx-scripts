#!/bin/bash


# activate psana environment
source /img/conda.local/env.local
source activate psana_base
source /img/opt/cctbx/build/setpaths.sh


# set location for experiment db and calib dir
export SIT_DATA=$CONDA_PREFIX/data
export SIT_PSDM_DATA=/global/cscratch1/sd/psdatmgr/data/psdm


# prevent crash when running on one core
export HDF5_USE_FILE_LOCKING=FALSE

SCRIPTDIR=/global/cfs/cdirs/lcls/fpoitevi/Software/detector-geometry-calibration/geomcalib
EXPDIR=/global/cfs/cdirs/lcls/exp/cxi/cxic0515

cd $EXPDIR/scratch
mkdir -p -m777 geomcalib
cd geomcalib

ln -sf $SCRIPTDIR/*.py .

python run-02-powderSum.py --exp cxic0515 --run 79 --noe 1000 --outDir ./

