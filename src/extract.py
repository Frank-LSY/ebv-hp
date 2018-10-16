#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 10:13:25 2018

@author: frank-lsy
"""
#import time
import sys
import getopt
import sh
def extract(input_file,output_dir):
    f = open(input_file,'r')
    sh.mkdir("-pv",output_dir)
    i = 0
    while 1:
        line = f.readline()
        if not line:
            f.close()
            break
        print(line)
        if (line[0]==">"):
            i += 1
            g = open("{0}/{1}.fa".format(output_dir,i),'a+')
            g.writelines(line)
        else:
            g.writelines(line)

def main(argv):
    input_file = ''
    output_dir = ''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print ("\nYour input is not a legal usage.\nUsage: extraxt.py -i <input_file> -o <output_dir>\n")
        sys.exit(2)
    if (opts == []):
        print ('\nUsage: extraxt.py -i <input_file> -o <output_dir>\n')
        sys.exit()
    for opt, arg in opts:
        if opt == '-h':
            print ('\nUsage: extraxt.py -i <input_file> -o <output_dir>\n')
            sys.exit()
        elif opt in ("-i","--input"):
            input_file = arg
        elif opt in ("-o","--output"):
            output_dir = arg
    
    extract(input_file,output_dir)      
    
if __name__ == "__main__":
    main(sys.argv[1:])