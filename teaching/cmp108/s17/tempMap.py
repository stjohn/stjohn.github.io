#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 10:15:47 2017

@author: stjohn
"""

#Import the folium package for making maps
import folium

#Create a map, centered (0,0) and zoomed out a bit:
mapCUNY = folium.Map(location=[0, 0],zoom_start=3)

#mapCUNY = folium.Map(location=[40.75, -74.125],zoom_start=10)
#mapCUNY.simple_marker(location = [40.873442, -73.889361], popup = "Lehman College")

#Save the map:
mapCUNY.save(outfile='tempMap.html')
