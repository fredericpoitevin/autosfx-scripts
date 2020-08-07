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

python unitcell_consensus.py
