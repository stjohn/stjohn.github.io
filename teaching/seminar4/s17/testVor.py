#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:51:30 2017

@author: stjohn
"""

import numpy
from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt


points = [
[22.7433333333000,  53.4869444444000],
[23.2530555556000,  53.5683333333000],
[23.1066666667000,  53.7200000000000],
[22.8452777778000,  53.7758333333000],
[23.0952777778000,  53.4413888889000],
[23.4152777778000,  53.5233333333000],
[22.9175000000000,  53.5322222222000],
[22.7197222222000,  53.7322222222000],
[22.9586111111000,  53.4594444444000],
[23.3425000000000,  53.6541666667000],
[23.0900000000000,  53.5777777778000],
[23.2283333333000,  53.4713888889000],
[23.3488888889000,  53.5072222222000],
[23.3647222222000,  53.6447222222000]]


vor = Voronoi(points)

voronoi_plot_2d(vor)
plt.axis('equal')
plt.xlim(22.65, 23.50)
plt.ylim(53.35, 53.85)
plt.show()

vor = Voronoi(locs)
print(vor.vertices)
print(vor.regions)

import matplotlib.pyplot as plt
voronoi_plot_2d(vor)
plt.show()


vorJSON = open('cunyVor.json', 'w')
print('{\n "type": "FeatureCollection",\n"features": [\n\n', file=vorJSON)


from geojson import FeatureCollection, Feature, Polygon

point_voronoi_list = []
feature_list = []
for region in range(len(vor.regions) - 1):
    vertice_list = []
    for x in vor.regions[region]:
        vertice = vor.vertices[x]
        vertice = (vertice[1], vertice[0])
        vertice_list.append(vertice)
        polygon = Polygon([vertice_list])
        feature = Feature(geometry=polygon, properties={})
        feature_list.append(feature)

feature_collection = FeatureCollection(feature_list)
print (feature_collection, file=vorJSON)
print(']}',file=vorJSON)

'''


regList = []
for reg in vor.regions:
    #print('{ "type": "Feature", "properties": { "name": "region"}, "geometry": { "type": "Polygon", "coordinates": [ ',
 #         file=vorJSON, end="")
    pList = []

    for p in reg:
        print (p,list(vor.vertices[p]))
        pList.append(list(vor.vertices[p]))
   
    print(pList)
    regStr = '{ "type": "Feature", "properties": { "name": "region"}, "geometry": { "type": "Polygon", "coordinates": [ ' + str(pList) + ']}'
    print(regStr)
    regList.append(regStr)
    #print(pList, '] } },\n', file = vorJSON)

s = '[' + ", \n".join(regList) + ']}\n'
print(s)
print(s,file=vorJSON)
'''
vorJSON.close()

mapVor = folium.Map(location=[40.75, -74.125],tiles="stamen terrain")

mapVor.choropleth(geo_path= 'cunyVor.json',
               fill_opacity=0.3, line_opacity=0.75)

mapVor.create_map(path='mapVor.html')