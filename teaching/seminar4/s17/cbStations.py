#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:09:39 2017

@author: stjohn
"""

import pandas as pd
import folium

stations = pd.read_json('https://feeds.citibikenyc.com/stations/stations.json')
mapBikes = folium.Map(location=[40.75, -73.99],tiles="Cartodb Positron",zoom_start=14)


for i,row in stations.iterrows():
    beanList = row['stationBeanList']
    lat = beanList['latitude']
    lon = beanList['longitude']
    name = beanList['stationName'] + ": " + str(beanList['availableBikes']) + " bikes available of " + str(beanList['totalDocks']) + " total bikes"
    print(name)
    if beanList['statusValue'] == 'Not In Service':
        name = beanList['stationName'] + ": Not In Service"
        i = folium.Icon(color='lightgray')
    else:
        name = beanList['stationName'] + ": " + str(beanList['availableBikes']) + " bikes available of " + str(beanList['totalDocks']) + " total bikes"
        if beanList['availableBikes'] < 2:
            i = folium.Icon(color='red')
        else:
            i = folium.Icon(color='green')
    folium.Marker([lat,lon],popup = name,icon = i).add_to(mapBikes)


#Create the html file with the map:
mapBikes.save(outfile='bikeLocations.html')
