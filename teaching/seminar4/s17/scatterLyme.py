#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 21:25:20 2017

@author: stjohn
"""

import matplotlib.pyplot as plt 
import numpy as np

infile = open('statesSummary.csv','r')

yearLine = infile.readline()
yearWords = yearLine.split(",")
years = []
for w in yearWords[1:]:
     years.append(int(w))

for i in range(5):
    line = infile.readline()
    words = line.split(",")
    stateName = words[0]
    stateValues = []
    for w in words[1:]:
        stateValues.append(int(w))
    color = np.random.rand(3)   
    plt.scatter(years, stateValues,
           c=color, label=stateName)

plt.title("Cases of Lyme Disease") 
plt.xlabel('Years')                
plt.ylabel('Number of Cases')      
plt.legend(loc = 2,
           fontsize = 'x-small')
plt.show()
