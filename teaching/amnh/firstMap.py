# RGGS 670: Algorithmics Approaches for Biological Data
# Spring 2016
# Katherine St. John
# Demonstrates mapping points to a map

import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

m = Basemap()
m.drawcoastlines()
m.fillcontinents(color='darkgreen',lake_color='darkblue')
m.drawmapboundary(fill_color='darkblue')
x,y = m(-74,40.7)
m.plot(x,y,'ro',markersize=10)
plt.show()


