from scipy.spatial import Voronoi, voronoi_plot_2d
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

points = [(40.740977, -73.984252),
          (40.717367, -74.012178),
          (40.856673, -73.910127),
          (40.630276, -73.955545),
          (40.608648, -74.153563),
          (40.747639, -73.943676),
          (40.752846, -73.984133),
          (40.817828, -73.926862),
          (40.768731, -73.964915),
          (40.769939, -73.986469),
          (40.578349, -73.934465),
          (40.743951, -73.935154),
          (40.873442, -73.889361),
          (40.66624, -73.957349),
          (40.695507, -73.987882),
          (40.744988, -73.816444),
          (40.736316, -73.820035),
          (40.755343, -73.988846),
          (40.748151, -73.989723),
          (40.819548, -73.949518),
          (40.748724, -73.984205),
          (40.702821, -73.795776)]

shapeFile = "2013-2014 School Zones/geo_export_1b268539-dcf4-4932-aae0-e4abe442660e"
m = Basemap(llcrnrlon=-74.3,llcrnrlat=40.425,\
            urcrnrlon=-73.675,urcrnrlat=40.975,\
            projection='tmerc',\
            lon_0=-74.01,lat_0=40.71)
m.readshapefile(shapeFile,'nyc')

x = [lon for (_,lon) in points]
y = [lat for (lat,_) in points]
xT,yT = m(x,y)
m.scatter(xT,yT,30,marker='o', color='r')


p2 = zip(x,y)
vor = Voronoi(p2)
voronoi_plot_2d(vor)
plt.show()
