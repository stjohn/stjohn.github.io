#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 25 07:07:17 2017

@author: stjohn
"""

import folium
import pandas as pd

geo_path = r'censusTracts.json'

zoning_map = folium.Map(location=[40.75, -74.125], zoom_start=12)
zoning_map.geo_json(geo_path=geo_path)
zoning_map.save(outfile='zoning.html')

