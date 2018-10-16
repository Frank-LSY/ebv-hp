#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  8 18:04:04 2018

@author: frank-lsy
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

ebv = pd.read_csv('../EBV-count.csv')
hp = pd.read_csv('../HP-count.csv')
bac_virus = pd.read_csv('../bac-virus.csv')
#ebv.boxplot()
#hp.boxplot()
#plt.show()

f = sns.boxplot(x="name",
                  y="num",
                  data=bac_virus,
                  showmeans=True,
                  notch=False,
                  flierprops = {'marker':'o','markerfacecolor':'black','color':'darkred'},
                  meanprops = {'marker':'D','markerfacecolor':'darkgreen'},
                  medianprops = {'linestyle':'-','color':'darkred','linewidth':2},
                  whiskerprops = {'linestyle':'--','color':'green'})
plt.yscale('log')
plt.ylabel("Amount")
plt.xlabel("Type")
plt.savefig("../bac-virus.png",dpi = 2560)
plt.show()
