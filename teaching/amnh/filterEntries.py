# RGGS 670: Algorithmics Approaches for Biological Data
# Spring 2016
# Katherine St. John
# Filters and prints entries from a specimen database file.
# Assumes the file is CSV and located in same folder as program.

import csv

#Open the file:
f = open("AMNH-Ornithology-Internet-Export.csv", "rU")

#Using the dictionary reader to access by column names:
reader = csv.DictReader(f)

#Traverse the file by rows, filtering for those specimens with GIS data:
for row in reader:
     if row['LATITUDE'] != '':
          print row['IDENTIFICATION']+":\t("+row['LATITUDE']+", "+row['LONGITUDE']+")"

f.close()
