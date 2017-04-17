#A combination of two programs:
#    1) pulls Lyme Disease data from CSV file and computes totals by states
#    2) plots the data to a state map, following an abbreviated version of the basemap demo
#    from stackoverflow: http://stackoverflow.com/questions/7586384/color-states-with-pythons-matplotlib-basemap)


import matplotlib.pyplot as plt 
import numpy as np
import csv

infile = open('statesSummary.csv','rU')
reader = csv.reader(infile)
yearLine = reader.next()
years = [int(w) for w in yearLine[1:]]

stateNames = []
stateTotals = []
for row in reader:
     stateNames.append(row[0])
     stateTotals.append(sum([int(r) for r in row[1:]]))

maxCases = float(max(stateTotals))
scaledTotals = [i/maxCases for i in stateTotals]




import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon

# create the map
map = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
        projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

# load the shapefile, use the name 'states'
map.readshapefile('st99_d00', name='states', drawbounds=True)

ax = plt.gca() # get current axes instance

# collect the state names from the shapefile attributes so we can
# look up the shape obect for a state by it's name
names = []
for shape_dict in map.states_info:
    names.append(shape_dict['NAME'])

#For each state that we have Lyme Disease data:
for i in range(len(stateNames)):
     print "Plotting", stateNames[i]
     seg = map.states[names.index(stateNames[i])]
     c = (1.0,1.0-scaledTotals[i],1.0)
     poly = Polygon(seg, facecolor=c,edgecolor='black')
     ax.add_patch(poly)
     
plt.show()   
