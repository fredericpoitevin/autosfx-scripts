#!/bin/bash

input=$1
output="http://pslogin01.slac.stanford.edu:8442/jid_slac/jid/ws/replace_counters/5f34da3effa887496ed9aca2"

frcdone_value="0.000"
while [ $frcdone_value != "100.0" ]; do

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
  line7=' {"key": "experiment_name", "value": "cxic0515" }'

  data="[${line1},${line2},${line3},${line4},${line5},${line6},${line7} ]"
  #echo $data
  #echo "curl -s -X POST  -H 'Content-Type: application/json' -d $data $output"
  
  #curl --trace-ascii /dev/stdout -s -X POST -H "Content-Type: application/json" -d "${data}" ${output}
  curl -s -X POST -H "Content-Type: application/json" -d "${data}" ${output}
  sleep 1

done
