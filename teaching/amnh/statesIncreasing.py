# Abbreviated version of basemap example (from stackoverflow: http://stackoverflow.com/questions/7586384/color-states-with-pythons-matplotlib-basemap)

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

# create the map
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# load the shapefile, use the name 'states'
map.readshapefile('st99_d00', name='states', drawbounds=True)

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
state_names = []
for shape_dict in map.states_info:
    state_names.append(shape_dict['NAME'])

ax = plt.gca() # get current axes instance
"""
# get Texas and draw the filled polygon
seg = map.states[state_names.index('Texas')]
poly = Polygon(seg, facecolor='purple',edgecolor='red')
ax.add_patch(poly)
"""
i = 0
for s in state_names:
     color = (1.0,0.0,i/60.0)
     i += 1
     for nshape,seg in enumerate(map.states[state_names.index(s)]):
          if state_names[nshape] not in ['District of Columbia','Puerto Rico']:
               poly = Polygon(seg,facecolor=color,edgecolor='black')
               ax.add_patch(poly)

plt.show()
