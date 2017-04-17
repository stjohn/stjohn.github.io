#Simple use of csv module.
#Assumes "in.csv" is in the same folder.
#Katherine St. John
#Spring 2016

import csv

#Using the dictionary reader to access by column names
f = open("in.csv")
reader = csv.DictReader(f)
m = [row['Homework'] for row in reader if int(row['Homework']) < 90]
f.close()
print m[-1]

#Using the regular csv reader (ignoring first line with column names).
#Note the use of 'with' for files:

with open("in.csv") as f:
     reader = csv.reader(f)
     reader.next()  #Ignore line with column names
     m = [row[2] for row in reader if int(row[2]) < 90]
print m[-1]
