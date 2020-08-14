#!/bin/bash -l
#SBATCH --account=lcls
#SBATCH --job-name=autosfx-unitcell-peakfinding
#SBATCH --nodes=2
#SBATCH --constraint=haswell
#SBATCH --time=01:00:00
#SBATCH --image=docker:slaclcls/crystfel:latest
#SBATCH --exclusive
#SBATCH --qos=realtime

echo "$@"
env

t_start=`date +%s`

export PMI_MMAP_SYNC_WAIT_TIME=600

./report.sh ${JID_UPDATE_COUNTERS} &

echo "srun -n 64 shifter ./peak_finding-testfred.sh $@"
srun -n 64 shifter ./peak_finding-testfred.sh "$@"

t_end=`date +%s`
echo PSJobCompleted TotalElapsed $((t_end-t_start)) $t_start $t_end  

  
