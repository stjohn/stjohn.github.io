#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 12:39:37 2017

@author: stjohn
"""

import pandas as pd

lyme = pd.read_csv("statesSummary.csv")
print (lyme.transpose())
print(lyme)