#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-scancel
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=00:10:00
#SBATCH --qos=realtime

scancel --name autosfx-reconstruction-phasing 
