 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
#adapted for citibike Fall 2019
"""
Created on Tue Mar 14 23:15:34 2017

@author: stjohn
"""
import pandas as pd
from scipy.spatial import Voronoi, voronoi_plot_2d
import folium

#File with library locations in NYC:
libs = pd.read_csv('LIBRARY.csv')

#Read directly from the citibike feed (can be replaced by static file):
stat_json = pd.read_json('https://feeds.citibikenyc.com/stations/stations.json')

#a datagrame that will hold relevant series extracted from the json
stations = pd.DataFrame(columns=['stationName', 'latitude', 'longitude', 'statusValue'])


#Create a map object, focused on NYC:
mapVor = folium.Map(location=[40.75, -73.96],tiles="Cartodb Positron",zoom_start=14)

#Pull out data from JSON beanlists into the stations dataframe
for i,row in stat_json.iterrows():
    #Pull out the station info:
    beanList = row['stationBeanList']

    #Create new row with desired station information
    newRow = {'stationName': beanList['stationName'], 'latitude': beanList['latitude'], 'longitude': beanList['longitude'],'statusValue':beanList['statusValue']}
    #add row to dataframe
    stations = stations.append(newRow, ignore_index=True, sort=False)



#Create lists to hold coordinates for vornoi diagram:
coords = []

#Add markers for each station to map
for index, row in stations.iterrows():
    name = row['stationName'] #repeat for LAT, LON, STATUS
    lat = float(row['latitude']) #repeat for others
    lon = float(row['longitude'])
    status = row['statusValue']
    #Add the [lat,lon] to list of coordinates:
    coords.append([lat,lon])

    #Add a marker to the map:
    folium.Marker([lat,lon],popup = name).add_to(mapVor)
    print("Processing:", name)


#Use scipy to make the voronoi diagram:
vor = Voronoi(coords)

#Plot with matplotlib to check that it's working:
import matplotlib.pyplot as plt
voronoi_plot_2d(vor)
plt.show()


#Use geojson file to write out the features
from geojson import FeatureCollection, Feature, Polygon

#The output file, to contain the Voronoi diagram we computed:
vorJSON = open('libVorBike.json', 'w')
point_voronoi_list = []
feature_list = []
for region in range(len(vor.regions)-1):
#for region in range(9):
    vertex_list = []
    for x in vor.regions[region]:
        #Not sure how to map the "infinite" point, so, leave off those regions for now:
        if x == -1:
            break;
        else:
            #Get the vertex out of the list, and flip the order for folium:
            vertex = vor.vertices[x]
            vertex = (vertex[1], vertex[0])
        vertex_list.append(vertex)
    #Save the vertex list as a polygon and then add to the feature_list:
    polygon = Polygon([vertex_list])
    feature = Feature(geometry=polygon, properties={})
    feature_list.append(feature)

#Write the features to the new file:
feature_collection = FeatureCollection(feature_list)
print (feature_collection, file=vorJSON)
vorJSON.close()

#Add the voronoi layer to the map:
#mapVor.geo_json(geo_path= 'libVor.json', fill_color = "BuPu",
#                fill_opacity=0.01, line_opacity=0.25)
#lib_geo = os.path.join('data', 'libVor.json')
mapVor.choropleth(geo_data='libVorBike.json', fill_color = "BuPu",
                fill_opacity=0.01, line_opacity=0.25)
#folium.LayerControl().add_to(mapVor)



mapVor.save(outfile='libVorBike.html')
