#!/bin/bash

function union ()
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
  #echo ${file_array[3]}

  for i in {0..4}
  do
    #echo ${file_array[i]}
    if [ $i -eq 0 ]
    then
      #echo ${file_array[i]}
      #echo ${file_array[`expr $i + 1`]}
      cat $1"/"${file_array[i]} $1"/"${file_array[`expr $i + 1`]}|sort|uniq > $1"/tmp-"`expr $i + 1`.csv
    else
      #echo $1"/tmp-"$i
      #echo $1"/"${file_array[i+1]}
      cat $1"/tmp-"$i.csv $1"/"${file_array[i+1]}|sort|uniq > $1"/tmp-"`expr $i + 1`.csv
    fi
  done
  
  for j in {1..4}
  do
    rm $1"/tmp-"$j.csv
  done
  mv $1"/tmp-5.csv" "$3/union-$2.csv"
}


folder="../HP-10000-people"
out_dir="../HP-sim-union"
mkdir -pv $out_dir
for k in {1..10000}
do
  input_dir=$folder"/"$k
  union $input_dir $k $out_dir
done
