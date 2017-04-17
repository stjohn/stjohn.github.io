#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 05:42:15 2017

@author: stjohn
"""

f = open("zoning2.json", "r")
o = open("zoneDistricts.csv", "w")

for line in f:
    s = line.find("urn")
    if s > -1:
        e = line.find('"', s)
        print(line[s:e]+",", end="", file=o)
    s = line.find("ZONEDIST")
    if s > -1:
        s = line.find(': "',s)
        e = line.find('"',s+3)
        print(line[s+3:e], file=o)
f.close()
o.close()