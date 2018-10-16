#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 16:47:48 2018

@author: frank-lsy
"""

import csv
import re
import sh
import sys
import getopt
import os

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

def no_ic50(input_dir,output_dir,file_amount):
    for i in range(1,file_amount+1):
        for hla in hla_arr:
            with open("{2}/{0}/{1}-qualified.csv".format(i,hla,input_dir),'r') as fileIn:
                reader = csv.reader(fileIn)
                column = [row[0] for row in reader]
                fileIn.close()
            
            for j in range(len(column)):
                column[j] = column[j][:9]+'\n'
            #print(column)
            sh.mkdir("-pv","{1}/{0}".format(i,output_dir))
            with open("{2}/{0}/{1}.csv".format(i,hla,output_dir),'w') as fileOut:
                for item in column:
                    fileOut.writelines(item)


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

    len_arr = os.popen("ls -l {}| grep '^d' | wc -l".format(input_dir)).readlines()
    length = strip(len_arr)
    file_amount = int(length[0])
    print (file_amount)
    no_ic50(input_dir,output_dir,file_amount)


if __name__ == "__main__":
    main(sys.argv[1:])








