#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 20:58:56 2017

@author: stjohn
"""

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

labor = pd.read_csv('labor.csv', skiprows=13)
print("The majors are:\n", labor["Major"])
laborCrop1 = labor.iloc[:,[0,2]]
print(laborCrop1)
laborCrop = labor.iloc[:,[2,3]]
print(labor.iloc[:,[2,3]].corr())

sns.regplot(x="Underemployment Rate", y="Median Wage Early Career", data=labor)

sns.jointplot(x="Underemployment Rate", y="Median Wage Early Career", data=labor)

print(labor["Underemployment Rate"].value_counts())
