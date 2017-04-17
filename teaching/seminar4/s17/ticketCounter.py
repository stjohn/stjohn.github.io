#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 18:22:27 2017

@author: stjohn
"""

#Using csv and dictionaries to count parking tickets
#Assumes "tickets20th.csv" is in the same folder.
#Katherine St. John
#Spring 2017

import csv

#Setting up a dictionary to store tickets:
tickets = {}

#Using the dictionary reader to access by column names
f = open("tickets.csv")
reader = csv.DictReader(f)
for row in reader:
    plate = row["Plate ID"]
    tickets[plate] = tickets.get(plate, 0) + 1
    print("Ticket", tickets[plate], "for", plate)
f.close()

#Sort by value (ie by number of tickets)
#   (See the dictionary examples on class webpage for a nice way to 
#   do this with list comprehensions)
worst = sorted(tickets, key = tickets.__getitem__, reverse=True)

#Print top 10 values:
for i in range(10):
    print("Plate", worst[i], "has", tickets[worst[i]], "tickets.")

