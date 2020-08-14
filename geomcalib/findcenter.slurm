#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-geomcalib-setup
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --constraint=haswell
#SBATCH --time=00:20:00
#SBATCH --image=docker:slaclcls/lcls-py2-cctbx:latest
#SBATCH --qos=realtime

t_start=`date +%s`

export PMI_MMAP_SYNC_WAIT_TIME=600

echo "calling findcenter.sh"
srun -n 1 shifter ./findcenter.sh
echo "done findcenter.sh"

t_end=`date +%s`
echo PSJobCompleted TotalElapsed $((t_end-t_start)) $t_start $t_end


