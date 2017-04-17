#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:55:59 2017

@author: stjohn

School districts, shaded by test scores
"""

#Import folium for maps and pandas for data wrangling
import folium
import pandas as pd

#Read in the test scores
fullData = pd.read_csv('math20132016.csv', skiprows = 6)
#Grab only 2016 data:
scores2016 = fullData[fullData.Year == 2016]
#Focus on 8th grade:
scores8th2016 = scores2016[fullData.Grade == "8"]
print(scores8th2016)

#Create a map:
schoolMap = folium.Map(location=[40.75, -74.125])

#Create a layer, shaded by test scores:
schoolMap.choropleth(geo_path="schoolDistricts.json",
                     fill_color='YlGn', fill_opacity=0.5, line_opacity=0.5,
                     threshold_scale = [100,200,300,400],
                     data = scores8th2016,
                     key_on='feature.properties.SchoolDist',
                     columns = ['district', 'Mean Scale Score']
                     ) 
#Output the map to an .html file:
schoolMap.save(outfile='testScores.html')