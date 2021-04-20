import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

#shapeFile = "communitydistrictsny/geo_export_f66a17b1-8524-4660-8413-a9161a1e9dc3"
#shapeFile = "nysd_16a/nysd"
shapeFile = "2013-2014 School Zones/geo_export_1b268539-dcf4-4932-aae0-e4abe442660e"

m = Basemap(llcrnrlon=-74.3,llcrnrlat=40.425,\
            urcrnrlon=-73.675,urcrnrlat=40.975,\
            projection='tmerc',\
            lon_0=-74.01,lat_0=40.71)
m.readshapefile(shapeFile,'nyc')
ax = plt.gca() # get current axes instance
for i in range(len(m.nyc)):
     print "Plotting", i
     seg = m.nyc[i]
     c = (1.0,1.0,1.0)
     poly = Polygon(seg, facecolor=c,edgecolor='black')
     ax.add_patch(poly)

#seg = m.nyc[nyc_dict['SHAPENUM']]
plt.show()
