#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-unitcell
#SBATCH --nodes=8
#SBATCH --constraint=haswell
#SBATCH --time=01:30:00
#SBATCH --image=docker:slaclcls/crystfel:latest
#SBATCH --exclusive
#SBATCH --qos=regular
#SBATCH --reservation=SFX_AUTO_1.1
t_start=`date +%s`
export PMI_MMAP_SYNC_WAIT_TIME=600
srun -n 512 shifter ./peak.sh
t_end=`date +%s`
echo PSJobCompleted TotalElapsed $((t_end-t_start)) $t_start $t_end
