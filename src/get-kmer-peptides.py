#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 11:04:11 2018

@author: frank-lsy
"""
import time
import re
import sys
import getopt
import os
import sh

def get_kmer_peptides(whole_peptides,k,file):
    peptides = []
    f = open(file,'a+')
    for i in range(len(whole_peptides)-k):
        peptides.append(whole_peptides[i:i+9])
        print(whole_peptides[i:i+9],file = f) #输出到文件
    f.close()
    return peptides

def strip(arr):
    p=re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
    #print(arr)
    return arr
    
def main(argv):
    input_dir = ''
    output_dir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nYour input is not a legal usage.\nUsage: get-kmer-peptides.py -i <input_dir> -o <output_dir>\n")
        sys.exit(2)
    if (opts == []):
        print ('\nUsage: get-kmer-peptides.py -i <input_dir> -o <output_dir>\n')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print ('\nUsage: get-kmer-peptides.py -i <input_dir> -o <output_dir>\n')
            sys.exit()
        elif opt in ("-i","--input"):
            input_dir = arg
        elif opt in ("-o","--output"):
            output_dir = arg
    sh.mkdir("-pv",output_dir)
    len_arr = os.popen("ls -l {}| grep '^-' | wc -l".format(input_dir)).readlines()
    length = strip(len_arr)
    length = int(length[0])
    print (length)
    for i in range(1,length+1):
        f = open("{0}/{1}.pep".format(input_dir,i),'r')
        g = "{0}/{1}.pep".format(output_dir,i)
        file_in = f.readlines()
        file_in = strip(file_in)
        ori_pep = ''
        for line in file_in:
            ori_pep += line
        get_kmer_peptides(ori_pep,9,g)   
    
if __name__ == "__main__":
    main(sys.argv[1:])