# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import folium

world = folium.Map(location=[0, 0],tiles="stamenwatercolor",zoom_start=2)

folium.Marker([40.75, -73.99]).add_to(world)
world.save("world.html")