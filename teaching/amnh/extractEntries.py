import csv

#Using the dictionary reader to access by column names
f = open("AMNH-Ornithology-Internet-Export.csv", "rU")
reader = csv.DictReader(f)
for row in reader:
     if row['LATITUDE'] != '':
          print row['IDENTIFICATION']+":\t("+row['LATITUDE']+", "+row['LONGITUDE']+")"
f.close()
