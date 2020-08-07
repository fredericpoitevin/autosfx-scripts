#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-unitcell
#SBATCH --nodes=1
#SBATCH --constraint=knl
#SBATCH --time=00:10:00
#SBATCH --image=docker:slaclcls/crystfel:latest
#SBATCH --exclusive
#SBATCH --qos=realtime

srun -n 2 -c 1 shifter ./peak_finding.sh
    
