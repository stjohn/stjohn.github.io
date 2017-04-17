#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 14:48:19 2017

@author: stjohn
"""

import folium
from folium.plugins import MarkerCluster
import pandas as pd

library = pd.read_csv('LIBRARY.csv', nrows=10)

#Create lists to hold coordinates and popups:
coords = []
popups = []
icons = []

print(library['the_geom'])
for index, row in library.iterrows():
    words = row['the_geom'].split(" ")
    lat = float(words[2][:-1])
    lon = float(words[1][1:])
    name = row['NAME']
    #Add the [lat,lon] to list of coordinates:
    coords.append([lat,lon])
    #Add the names to the popup list>
    popups.append(name)
    icons.append(folium.Icon(icon='cloud'))
  
print(coords)

#Read in the campuses and center the map
mapLib = folium.Map(location=[40.75, -74.125],tiles="stamenwatercolor")

mapLib.choropleth(geo_path="schoolDistricts.json",
                     fill_opacity=0.1, line_opacity=0.75
                     ) 

#Add all the markers at once:
mapLib.add_children(MarkerCluster(locations=coords, popups = popups, icons=icons))

#Create the html file with the map:
mapLib.save(outfile='libraries.html')