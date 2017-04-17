# RGGS 670: Algorithmics Approaches for Biological Data
# Spring 2016
# Katherine St. John
# Filters and prints entries from a specimen database file.
# Assumes the file is CSV and located in same folder as program.

import csv
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap



#Open the file:
f = open("AMNH-Ornithology-Internet-Export.csv", "rU")

#Using the dictionary reader to access by column names:
reader = csv.DictReader(f)

#Set up arrays to hold the information extracted from the csv file:
latStrings = []
longStrings = []
ident = []

#Traverse the file by rows, filtering for those specimens with GIS data:
for row in reader:
  if row['LATITUDE'] != '':
    ident.append(row['IDENTIFICATION'])
    latStrings.append(row['LATITUDE'])
    longStrings.append(row['LONGITUDE'])
f.close()

#Convert latitudes into x-values:
lats = []
for l in latStrings:
  words = l.split()
  tmp = float(words[0]) + float(words[1])/60.0
  if l[-1] == 'S':
    tmp = -tmp
  lats.append(tmp)

#Convert longitudes into y-values:
longs = []
for l in longStrings:
  words = l.split(" ")
  tmp = float(words[0]) + float(words[1])/60.0
  if l[-1] == 'W':
    tmp = -tmp
  longs.append(tmp)

#Set up a map:
m = Basemap()
m.drawcoastlines()
m.fillcontinents(color='darkgreen',lake_color='darkblue')
m.drawmapboundary(fill_color='darkblue')

#Plot each point:
for i in range(len(longs)):
  print "Plotting:", ident[i], "\t@", longStrings[i]+", "+latStrings[i]
  x,y = m(longs[i],lats[i])
  m.plot(x,y,'ro',markersize=10)
plt.show()

