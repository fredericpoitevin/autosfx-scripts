#!/bin/bash

# define path to scripts and experiment
SCRIPTDIR=/global/cfs/cdirs/lcls/fpoitevi/Software/detector-geometry-calibration/geomcalib/
EXPDIR=/global/cfs/cdirs/lcls/exp/cxi/cxic0515

cd $EXPDIR/scratch
mkdir -p -m777 geomcalib
cd geomcalib

ln -sf $SCRIPTDIR/*.py .
cp $SCRIPTDIR/load_everything.sh .

./load_everything.sh

python run-01-expSetup.py --exp cxic0515 --run 79 --outDir ./

