#!/bin/bash

# set location for experiment db and calib dir
export SIT_PSDM_DATA=/global/cscratch1/sd/psdatmgr/data/psdm

EXPERIMENT_NAME=$1

instrument=${EXPERIMENT_NAME:0:3}
SCRATCH=$SIT_PSDM_DATA/${instrument}/${EXPERIMENT_NAME}/scratch/

runlist=` ls -d $SCRATCH/r*/ 2>/dev/null`
if [ "$run_list" != "" ]; then
  for run in $runlist; do
    status_file="${SCRATCH}/${run}/peak-finding/status_peaks_*.txt"
    if ls $status_file 1> /dev/null 2>&1; then
      frcdone_value="0.000"
      while [ $frcdone_value != "100.0" ]; do

      done
    else
      echo "REPORT: no status file in ${SCRATCH}/${run}/peak-finding/"
    fi
  done
else
  echo "no run were found in $SCRATCH"
fi

################
# BELOW IS JUST TO BORROW SOME CODE
################

output_url=$1
EXPERIMENT_NAME=$2
RUN_NUM=$3
DETECTOR=$4

# define output directory
instrument=${EXPERIMENT_NAME:0:3}
outdir="${SIT_PSDM_DATA}/${instrument}/${EXPERIMENT_NAME}/scratch/r${RUN_NUM}/peak-finding/"
input=${outdir}"status_peaks_*.txt"


frcdone_value="0.000"
while [ $frcdone_value != "100.0" ]; do

  if ls $input 1> /dev/null 2>&1; then

    content=`cat $input | awk -v FS="{" '{print$2}' | awk -v FS="}" '{print$1}'`

    numhits=`echo $content | awk -v FS=',' '{print $1}'`
    hitrate=`echo $content | awk -v FS=',' '{print $2}'`
    frcdone=`echo $content | awk -v FS=',' '{print $3}'`
    prjcted=`echo $content | awk -v FS=',' '{print $4}'`

    frcdone_value=`echo $frcdone | awk -v FS=':' '{print$2}'`

    line1=' {"key": '`echo $numhits | awk -v FS=':' '{print$1}'`', "value":'`echo $numhits | awk -v FS=':' '{print$2}'`' }'
    line2=' {"key": '`echo $hitrate | awk -v FS=':' '{print$1}'`', "value":'`echo $hitrate | awk -v FS=':' '{print$2}'`' }'
    line3=' {"key": '`echo $frcdone | awk -v FS=':' '{print$1}'`', "value":'`echo $frcdone | awk -v FS=':' '{print$2}'`' }'
    line4=' {"key": '`echo $prjcted | awk -v FS=':' '{print$1}'`', "value":'`echo $prjcted | awk -v FS=':' '{print$2}'`' }'
    line5=' {"key": "date", "value": "'`date`'" }'
    line6=' {"key": "path", "value": "'`echo $input`'" }'
    line7=' {"key": "experiment_name", "value": "'`echo $EXPERIMENT_NAME`'" }'

    data="[${line1},${line2},${line3},${line4},${line5},${line6},${line7} ]"
    curl -s -X POST -H "Content-Type: application/json" -d "${data}" ${output_url}

  else
    echo "REPORT: waiting for creation of $input"
    sleep 10
  fi
  sleep 1

done
