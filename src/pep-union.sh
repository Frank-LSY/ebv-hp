#!/bin/bash

function union()
{
  file_array=()
  let i=0
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
#否则就能够读取该文件的地址
    #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
    #echo `basename $file`
    file_array[i]=`basename $file`
    let i=$i+1
  done
  len=${#file_array[@]}


  for ((i=0;i<len;i++))
  do
    for ((j=1;j<1445;j++))
    do
    #echo ${file_array[i]}
      if [ $j -eq 1 ]
      then
      #echo ${file_array[i]}
      #echo ${file_array[`expr $i + 1`]}
        cat $2"/"$j"/"${file_array[i]} $2"/"`expr $j + 1`"/"${file_array[i]}|sort|uniq > $2"/tmp/tmp-"`expr $j + 1`.csv
      else
      #echo $1"/tmp-"$i
      #echo $1"/"${file_array[i+1]}
        cat $2"/tmp/tmp-"$j.csv $2"/"`expr $j + 1`"/"${file_array[i]}|sort|uniq > $2"/tmp/tmp-"`expr $j + 1`.csv
      fi
    done
    for ((k=2;k<1445;k++))
    do
      rm $2"/tmp/tmp-"$k.csv
    done
    mv $2"/tmp/tmp-1445.csv" $3"/"${file_array[i]}
  done
}

tmp_dir="../HP-no-ic50/1"
ori_folder="../HP-no-ic50"
out_folder="../HP-HLA-union"

union $tmp_dir $ori_folder $out_folder
