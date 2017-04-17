#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 11:17:29 2017

@author: stjohn
"""

import folium
from folium.plugins import MarkerCluster
import pandas as pd
#import numpy as np


cuny = pd.read_csv('cunyLocations.csv')
print (cuny)
mapCUNY = folium.Map(location=[40.75, -74.125])

coords = []
popups = []

for index,row in cuny.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    coords.append([lat,lon])
    popups.append(name)
    #mapCUNY.simple_marker([lat, lon], popup=name, clustered_marker = True)

mapCUNY.add_children(MarkerCluster(locations=coords, popups = popups))
mapCUNY.save(outfile='cunyLocations.html')


'''
map = folium.Map(location=[40.75, -73.99], zoom_start=10, tiles="Mapbox Bright")
map.geo_json(geo_path = 'zoning2.json', fill_opacity=0.2)

map.create_map(path='zoning.html')
'''