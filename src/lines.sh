#!/bin/bash

for file in `ls "../HP-HLA-union"`
do 
	echo `basename $file`
	cat "../HP-HLA-union/"`basename $file`|wc -l>>"../HP-HLA-count.csv"
done
