#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 14:23:06 2017

@author: stjohn
"""

import pandas as pd
col = pd.read_csv('collisionsZIP.csv')
print(col.groupby('DATE')['TIME'].sum())


col.plot(x="TIME", y = "NUMBER OF PERSONS INJURED")