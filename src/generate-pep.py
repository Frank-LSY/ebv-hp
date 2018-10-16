#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:16:00 2018

@author: frank-lsy
"""
#import time
import os
import re
import sys
import getopt
import sh

def strip(arr):
    p=re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
    #print(arr)
    return arr


def generate_pep(input_dir,output_dir):
    sh.mkdir("-pv",output_dir)
    len_arr = os.popen("ls -l {}| grep '^-' | wc -l".format(input_dir)).readlines()
    length = strip(len_arr)
    length = int(length[0])
    print (length)
    for i in range(1,length+1):
        f = open("{0}/{1}.fa".format(input_dir,i),'r')
        g = open("{0}/{1}.pep".format(output_dir,i),'a+')
    
        while 1:
            line = f.readline()
            if not line:
                f.close()
                break
            if (line[0] != ">"):
                g.writelines(line)
                
def main(argv):
    input_dir = ''
    output_dir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nYour input is not a legal usage.\nUsage: generate-pep.py -i <input_dir> -o <output_dir>\n")
        sys.exit(2)
    if (opts == []):
        print ('\nUsage: generate-pep.py -i <input_dir> -o <output_dir>\n')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print ('\nUsage: generate-pep.py -i <input_dir> -o <output_dir>\n')
            sys.exit()
        elif opt in ("-i","--input"):
            input_dir = arg
        elif opt in ("-o","--output"):
            output_dir = arg
            
    generate_pep(input_dir,output_dir)
    
if __name__ == "__main__":
    main(sys.argv[1:])