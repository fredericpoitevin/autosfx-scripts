#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-unitcell-consensus
#SBATCH --nodes=1
#SBATCH --constraint=haswell
#SBATCH --time=00:10:00
#SBATCH --image=docker:slaclcls/lcls-py2-cctbx:latest
##autosfx:latest
#SBATCH --qos=realtime

t_start=`date +%s`

export PMI_MMAP_SYNC_WAIT_TIME=600

echo "calling unitcell_consensus.sh"
srun -n 1 -c 1 shifter ./unitcell_consensus.sh
echo "done unitcell_consensus.sh"

t_end=`date +%s`
echo PSJobCompleted TotalElapsed $((t_end-t_start)) $t_start $t_end


