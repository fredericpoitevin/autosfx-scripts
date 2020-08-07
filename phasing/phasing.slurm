#!/usr/bin/env bash
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-reconstruction-phasing
#SBATCH --nodes=1
#SBATCH --tasks-per-node=32
#SBATCH --constraint=haswell
#SBATCH --time=00:30:00
#SBATCH --image=docker:registry.services.nersc.gov/annagian/sfx_6
#SBATCH --gres=craynetwork:4
#SBATCH --qos=realtime

SCRIPTDIR=/global/cfs/cdirs/lcls/fpoitevi/Software/sfxPhasing/sfxPhasing/SAD_Phasing/
EXPDIR=/global/cfs/cdirs/lcls/exp/cxi/cxic0515

cd $EXPDIR/scratch
mkdir -p -m777 sfxPhasing
cd sfxPhasing

ln -sf $SCRIPTDIR/*.py .
cp     $SCRIPTDIR/*.json .

python batch_sub.py  \
  -rfl $EXPDIR/scratch/stream2mtz/a2a.mtz       \
  -seq $EXPDIR/inputs/a2a.fasta     \
  -SFAC S            \
  -n 1              \
  --shifter 1
