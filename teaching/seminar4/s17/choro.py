#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 10:52:27 2017

choro.py from https://gist.github.com/wrobstory/5609889#file-us_counties_20m_topo-json
"""

import folium
import pandas as pd

county_data = r'us_county_data.csv'
county_geo = r'us_counties_20m_topo.json'

#Read into Dataframe, cast to string for consistency
df = pd.read_csv(county_data, na_values=[' '])
df['FIPS_Code'] = df['FIPS_Code'].astype(str)


def set_id(fips):
    '''Modify FIPS code to match GeoJSON property'''
    if fips == '0':
        return None
    elif len(fips) <= 4:
        return ''.join(['0500000US0', fips])
    else:
        return ''.join(['0500000US', fips])

#Apply set_id, drop NaN
df['GEO_ID'] = df['FIPS_Code'].apply(set_id)
df = df.dropna()

#Number of employed with auto scale
map_1 = folium.Map(location=[48, -102], zoom_start=3)
map_1.geo_json(geo_path=county_geo, data_out='data1.json', data=df,
               columns=['GEO_ID', 'Employed_2011'],
               key_on='feature.id',
               fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.3,
               topojson='objects.us_counties_20m')

map_1.create_map(path='map_1.html')