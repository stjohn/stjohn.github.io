#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  5 05:19:35 2017

@author: stjohn
"""

import folium

mapMH = folium.Map(location=[40.815743, -73.952637],tiles="Cartodb Positron",
                   zoom_start=10)

folium.Marker(location=[40.815743, -73.952637], popup="The Mott Hall School (lat: 40.815743; lon: -73.952637)").add_to(mapMH)
mapMH.save(outfile="mhs.html")