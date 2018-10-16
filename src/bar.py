#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 10:57:00 2018

@author: frank-lsy
"""

import matplotlib.pyplot as plt
import pandas as pd

ebv = pd.read_csv("../EBV-HLA-count.csv")
hp = pd.read_csv("../HP-HLA-count.csv")

name_list = ebv["HLA"]
ebv_list = ebv["Amount"]
hp_list = hp["Amount"]


plt.bar(name_list,ebv_list,label = "ebv",fc='r')
plt.legend()
plt.savefig("../bar-ebv.png",dpi = 2560)
plt.show()

plt.bar(name_list,hp_list,label = "hp",fc='g')
plt.legend()
plt.savefig("../bar-hp.png",dpi = 2560)
plt.show()