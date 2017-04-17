#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:26:08 2017

@author: stjohn
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

pop = pd.read_csv('nycHistPop.csv',skiprows=5)
print(pop)
pop.plot.bar(x="Year")
pop['PercentBronx'] = pop['Bronx']/pop['Total']
pop.plot(x="Year", y = 'PercentBronx')



print(pop['Bronx']/pop['Total']*100)


sns.jointplot(x='Bronx',y='Total', data=pop)

print(pop.corr())