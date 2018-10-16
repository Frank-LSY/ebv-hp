#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:33:56 2018

@author: frank-lsy
"""

import re
import csv
import sh
import os
import getopt
import sys

IC50_THRESHOLD = 500

def qualified_peptide(input_file,output_file):
    qualified_rows = []
    try:     
        with open(input_file,'r') as fileIn:
            file = csv.DictReader(fileIn)
            for row in file:
                if (float(row['ic50'])<=IC50_THRESHOLD):
                    rows = [row['peptide'],row['ic50']]
                    qualified_rows.append(rows)
    except FileNotFoundError:
        print('NO SUCH FILE!{}'.format(input_file))
            #print(qualified_rows)
    with open (output_file,'w') as fileOut:
        file = csv.writer(fileOut)
        for item in qualified_rows:  
            file.writerow(item)


hla_a = open("../dataset/HLA-A.csv","r")
hla_b = open("../dataset/HLA-B.csv","r")
hla_c = open("../dataset/HLA-C.csv","r")

hla_a_arr = hla_a.readlines()
hla_b_arr = hla_b.readlines()
hla_c_arr = hla_c.readlines()

hla_a.close()
hla_b.close()
hla_c.close()

def strip(arr):
    p=re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
    #print(arr)
    return arr

hla_a_arr = strip(hla_a_arr)
hla_b_arr = strip(hla_b_arr)
hla_c_arr = strip(hla_c_arr)

hla_arr = hla_a_arr+hla_b_arr+hla_c_arr


def main(argv):
    ori_dir = ''
    op_dir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nYour input is not a legal usage.\nUsage: get_qualified_pep.py -i <input_dir> -o <output_dir>\n")
        sys.exit(2)
    if (opts == []):
        print ('\nUsage: get_qualified_pep.py -i <input_dir> -o <output_dir>\n')
        sys.exit()
   
    for opt, arg in opts:
        if opt == '-h':
            print ('\nUsage: get_qualified_pep.py -i <input_dir> -o <output_dir>\n')
            sys.exit()
        elif opt in ("-i","--input"):
            ori_dir = arg
        elif opt in ("-o","--output"):
            op_dir = arg
    print(ori_dir)
    print(op_dir)    
    len_arr = os.popen("ls -l {}| grep '^d' | wc -l".format(ori_dir)).readlines()
    length = strip(len_arr)
    length = int(length[0])
    print(length)         
    for i in range(1,length+1):
        input_dir = "{0}/{1}.pep".format(ori_dir,i)
        output_dir = "{0}/{1}".format(op_dir,i)
        sh.mkdir("-pv",output_dir)
        for item in hla_arr:
            input_file = "{0}/{1}\r.csv".format(input_dir,item)
            output_file = "{0}/{1}-qualified.csv".format(output_dir,item)
            qualified_peptide(input_file,output_file)
    
if __name__ == "__main__":
    main(sys.argv[1:])