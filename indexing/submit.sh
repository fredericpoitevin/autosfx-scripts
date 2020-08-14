#!/usr/bin/env bash
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-unitcell
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --constraint=haswell
#SBATCH --time=00:05:00
#SBATCH --image=docker:slaclcls/autosfx2:latest
#SBATCH --gres=craynetwork:4
#SBATCH --qos=realtime

module load python/2.7-anaconda-2019.07

python -u indexCrystals.py \
  -e cxic0515 \
  -d CxiDs2.0:Cspad.0 \
  --geom $SCRATCH/r0081/.temp.geom \
  --peakMethod cxi \
  --integrationRadius 3,4,5 \
  --indexingMethod mosflm \
  --minPeaks 15 \
  --maxPeaks 2048 \
  --minRes -1 \
  --tolerance 5,5,5,1.5 \
  --outDir $SCRATCH \
  --sample crystal \
  --queue psanaq \
  --chunkSize 5 \
  --noe -1 \
  --instrument CXI \
  --pixelSize 0.00010992 \
  --coffset 0.3189936 \
  --clenEpics CXI:DS2:MMS:06.RBV \
  --logger False \
  --hitParam_threshold 15 \
  --keepData True \
  -v 0 \
  --run 81 > temp.log

