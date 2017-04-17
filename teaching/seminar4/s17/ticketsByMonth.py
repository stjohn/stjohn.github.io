#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:13:12 2017

@author: stjohn
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

#Create a dictionary to count tickets:
tickets={}
#Open up the CSV file:
f=open("tickets.csv")
reader=csv.DictReader(f)

#Read each row, get the issue date, extract the month:
for row in reader:
    month=row["Issue Date"]
    monthNum=int(month[:2])
    tickets[monthNum]=tickets.get(monthNum,0)+1

#Set up the x and y for the histogram
xMonths=range(1,13)
yTickets=[]
for i in xMonths:
    yTickets.append(tickets.get(i,0))
    

#Plot as a bar chart:
plt.ylabel('Number of Tickets')
plt.xlabel('Months')
plt.bar(xMonths, yTickets, align='center', alpha=0.5)
plt.title('Tickets per Month')
plt.show()