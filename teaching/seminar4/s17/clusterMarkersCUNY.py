#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 10:07:09 2017

@author: stjohn

Here's a version of the CUNY campuses map that clusters as you zoom out
"""

#Note that we're explicitly importing MarkerCluster from the Folium plugins:
import folium
from folium.plugins import MarkerCluster
import pandas as pd


#Read in the campuses and center the map
cuny = pd.read_csv('cunyLocations.csv')
mapCUNY = folium.Map(location=[40.75, -74.125])


#Create lists to hold coordinates and popups:
coords = []
popups = []
icons = []

#For each row in the CSV file:
for index,row in cuny.iterrows():
    #Extract the data:
    lat = row["Latitude"]
    lon = row["Longitude"]
    name = row["Campus"]
    #Add the [lat,lon] to list of coordinates:
    coords.append([lat,lon])
    #Add the names to the popup list>
    popups.append(name)
    if row["College or Institution Type"] == "Senior Colleges":
        icons.append(folium.Icon(icon='cloud'))
    else:
        icons.append(folium.Icon(color='green'))
    
#Add all the markers at once:
mapCUNY.add_children(MarkerCluster(locations=coords, popups = popups, icons=icons))

#Create the html file with the map:
mapCUNY.save(outfile='cunyLocations.html')