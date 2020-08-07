#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-clear-scratch
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=00:10:00
#SBATCH --qos=realtime

EXPDIR=/global/cfs/cdirs/lcls/exp/cxi/cxic0515

SCRATCHDIR=$EXPDIR/scratch

chmod -R 777 $SCRATCHDIR

#PHASING=$SCRATCHDIR/sfxPhasing 
#if [ -d $SCRATCHDIR ]; then
#  rm -rf $SCRATCHDIR/*
#fi
