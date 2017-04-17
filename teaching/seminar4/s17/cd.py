#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 17:31:09 2017

@author: stjohn
"""

import folium
import pandas as pd

#Some useful functions for working with community district data:
def makeBoroID(row):
    """
    Adds a unique ID for each community district, matching what's used in 
    the city's geoJSON file.  
    :param row:  a row in the dataframe, assumes columns named "Borough" and "CD Number"
    :return: returns the borough ID
    """
    borough = row["Borough"]
    cdNum = row["CD Number"]
    if borough == "Manhattan":
        bID = 100 + cdNum
    elif borough == "Bronx":
        bID = 200 + cdNum
    elif borough == "Brooklyn":
        bID = 300 + cdNum
    elif borough == "Queens":
        bID = 400 + cdNum
    else:
        bID = 500 + cdNum
    return bID
        

def addOpenSpace(df):
    """
    Parks/open space are included in the geoJSON file, but not in most data
    collected about community districts
    :param df: the dataframe to add parks/open space.  Assumes attributes 
        'Borough ID', 'Borough' and 'CD Name'
    :return: returns the dataframe with additional rows for open space and 
        numerical values set to 0.
    """
    #Add in blank rows for parks:
    for i in range(164,165):
        #Manhattan:
        df = df.append([{'Borough ID' : i, 
                         'Borough' : 'Manhattan',
                         'CD Name' : 'Park/Open Space'}])    

    for i in range(226,229):
        #Bronx
        df = df.append([{'Borough ID' : i, 
                         'Borough' : 'Bronx', 
                         'CD Name' : 'Park/Open Space'}])
    
    for i in range(355,357):
        #Brooklyn
        df = df.append([{'Borough ID' : i, 
                         'Borough' : 'Brooklyn', 
                         'CD Name' : 'Park/Open Space'}])
    
    for i in range(480,485):
        #Queens
        df = df.append([{'Borough ID' : i, 
                         'Borough' : 'Queens', 
                         'CD Name' : 'Park/Open Space'}])

    for i in range(595,596):
        #Staten Island
        df = df.append([{'Borough ID' : i, 
                         'Borough' : 'Staten Island',
                         'CD Name' : 'Park/Open Space'}],
                         ignore_index=True) 
    df = df.fillna(0)
    return df
    

  
    
    
    
#Read in data:    
pop = pd.read_csv("New_York_City_Population_By_Community_Districts.csv")

#Add in the borough IDs to match geoJSON file:
pop['Borough ID'] = pop.apply(makeBoroID, axis =1)

#Add in rows for open space:
pop =  addOpenSpace(pop)

#Create a map, focused on NYC:
mapCD = folium.Map(location=[40.715, -73.99],tiles="Cartodb Positron",
                   zoom_start=10)

#Use openData NYC's community district boundaries and key on borough ID and 
#2010 population to make a choropleth map:
mapCD.geo_json(geo_path= 'cdBoundaries.json', fill_color = "GnBu", 
                fill_opacity=0.7, line_opacity=0.75,
                threshold_scale = [0,50000,100000,150000,200000,250000],
                data = pop,
                key_on='feature.properties.BoroCD',
                columns = ['Borough ID', '2010 Population'])

#Save the map as an .html file:
mapCD.save(outfile="cd.html")