#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-unitcell
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=00:30:00
#SBATCH --image=docker:slaclcls/crystfel:latest
#SBATCH --exclusive
#SBATCH --qos=realtime

t_start=`date +%s`

export PMI_MMAP_SYNC_WAIT_TIME=600

#srun -n 1 -c 3 shifter ./peak_finding.sh
srun -n 3 shifter ./peak.sh

t_end=`date +%s`
echo PSJobCompleted TotalElapsed $((t_end-t_start)) $t_start $t_end  

  
