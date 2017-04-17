#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 13:02:35 2017

@author: stjohn
"""

import pandas as pd

homeless = pd.read_csv("DHS_Daily_Report_2015.csv")
homeless.plot(x = "Date of Census")

print("The max total count is", homeless["Total Individuals in Shelter"].max() )