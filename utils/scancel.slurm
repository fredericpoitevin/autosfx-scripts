#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-scancel
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=00:10:00
#SBATCH --qos=realtime

#cat /global/homes/p/psdatmgr/arp/arp_submit.sh
scancel --name autosfx-unitcell-peakfinding
#scancel --name autosfx-reconstruction-MR-phasing 
