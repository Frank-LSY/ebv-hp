#!/bin/bash

function pre ()
{
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
    echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
  	echo `basename $file`
  	mkdir -pv "../EBV-pre/"`basename $file`
  	for line in `cat $2`
  	do
      echo `basename $file`
  		echo $line
  		python3.6 ../ref/mhcnuggets-2.0/mhcnuggets/src/predict.py \
  		-c I \
  		-p $1`basename $file` \
  		-a $line \
  		-o "../EBV-pre/"`basename $file`/$line.csv
  	done
  done
}

folder="../EBV-9mer/"
hla="../dataset/HLA-A.csv"
pre $folder $hla
hla="../dataset/HLA-B.csv"
pre $folder $hla
hla="../dataset/HLA-C.csv" 
pre $folder $hla
