#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 19:18:05 2017

@author: stjohn
"""



from bokeh.io import output_file, show
from bokeh.models import (
  GMapPlot, GMapOptions, ColumnDataSource, Circle, DataRange1d, PanTool, WheelZoomTool, BoxSelectTool
)

map_options = GMapOptions(lat=40.88, lng=-73.97, map_type="roadmap", zoom=11)

plot = GMapPlot(
    x_range=DataRange1d(), y_range=DataRange1d(), map_options=map_options, title="New York"
)

plot.api_key = "AIzaSyCdpRWhGsCGOCPRNH3Q2hY6gn4oMeSKaCU"

source = ColumnDataSource(
    data=dict(
        lat=[40.7735, 40.9, 40.8],
        lon=[-73.9794, -74, -73.9799],
    )
)

circle = Circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.8, line_color=None)
plot.add_glyph(source, circle)

plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())
output_file("gmap_plot.html")
show(plot)