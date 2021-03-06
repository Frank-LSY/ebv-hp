#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 15:15:27 2018

@author: frank-lsy
"""
import random
import re
import sh

hla_a = open("../dataset/HLA-A.csv","r")
hla_b = open("../dataset/HLA-B.csv","r")
hla_c = open("../dataset/HLA-C.csv","r")

hla_a_arr = hla_a.readlines()
hla_b_arr = hla_b.readlines()
hla_c_arr = hla_c.readlines()

hla_a.close()
hla_b.close()
hla_c.close()

hla_a_frequency = open("../dataset/HLA-A-frequency.csv","r")
hla_b_frequency = open("../dataset/HLA-B-frequency.csv","r")
hla_c_frequency = open("../dataset/HLA-C-frequency.csv","r")

hla_a_arr_frequency = hla_a_frequency.readlines()
hla_b_arr_frequency = hla_b_frequency.readlines()
hla_c_arr_frequency = hla_c_frequency.readlines()

hla_a_frequency.close()
hla_b_frequency.close()
hla_c_frequency.close()

def strip(arr):
    p = re.compile('\n')
    q = re.compile('\*')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
        arr[i]=re.sub(q,'',arr[i])
    #print(arr)
    return arr

def weighted_choice(weights):
  rnd = random.random() * sum(weights)
  for i, w in enumerate(weights):
      rnd -= w
      if rnd < 0:
          return i

hla_a_arr_frequency = strip(hla_a_arr_frequency)
hla_b_arr_frequency = strip(hla_b_arr_frequency)
hla_c_arr_frequency = strip(hla_c_arr_frequency)

hla_a_arr_frequency = list(map(float, hla_a_arr_frequency))
hla_b_arr_frequency = list(map(float, hla_b_arr_frequency))
hla_c_arr_frequency = list(map(float, hla_c_arr_frequency))

hla_a_arr = strip(hla_a_arr)
hla_b_arr = strip(hla_b_arr)
hla_c_arr = strip(hla_c_arr)


seq = []
for i in range(10000):
    seq.append(i)

rand_dict = dict.fromkeys(seq)
rand_hla = ['','','','','','']

for j in range(10000):
    rand_hla[0] = hla_a_arr[weighted_choice(hla_a_arr_frequency)]
    rand_hla[1] = hla_a_arr[weighted_choice(hla_a_arr_frequency)]
    rand_hla[2] = hla_b_arr[weighted_choice(hla_b_arr_frequency)]
    rand_hla[3] = hla_b_arr[weighted_choice(hla_b_arr_frequency)]
    rand_hla[4] = hla_c_arr[weighted_choice(hla_c_arr_frequency)]
    rand_hla[5] = hla_c_arr[weighted_choice(hla_c_arr_frequency)]
    rand_dict[j] = rand_hla
    rand_hla = ['','','','','','']
    #print(rand_dict)
for k in range(10000):
    for l in range(6):
        original_file = '../HP-HLA-union/{}.csv'.format(rand_dict[k][l])
        #f = open(original_files,'r')
        output_dir = '../HP-10000-people/{}'.format(k+1)
        sh.mkdir("-pv",output_dir)
        output_file = '{0}/{1}.csv'.format(output_dir,rand_dict[k][l])
        sh.cp(original_file,output_file)
    print("finish!")