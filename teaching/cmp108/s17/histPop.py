#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 14:26:08 2017

@author: stjohn
"""

#Import the pandas package, and use the standard abbreviation pd
import pandas as pd

#Read in the historical NYC population data:
#  The first 5 rows have comments, so skip those:
pop = pd.read_csv('nycHistPop.csv',skiprows=5)

#Print the dataframe to make sure it loaded correctly
print(pop)

#Plot the boroughs against year:
pop.plot(x="Year")

#Drop the total column, so, we can make a stacked bar chart:
pop = pop.drop('Total', 1)
#where 1 is the axis number (0 for rows and 1 for columns.)

#Regular bar chart:
pop.plot.bar(x="Year")

#Stacked bar chart:
pop.plot.bar(x="Year", stacked=True)