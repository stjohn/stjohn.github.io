#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr  4 13:21:49 2017

@author: stjohn
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 09:55:59 2017

@author: stjohn

School districts, shaded by test scores
"""




#Import folium for maps and pandas for data wrangling
import folium
import pandas as pd


def makeDifferenceColumn(row):
    #Fill this in with code that computes the difference in achieving 
    #proficiency between 2016 and 2013:
    return (row["%.4_y"] - row["%.4_x"])



#Read in the test scores
fullData = pd.read_csv('math20132016.csv', skiprows = 6)

#Keep only the data for "All Grades"
allGrades= fullData[fullData.Grade == "All Grades"]
#Grab only 2016 data:
scores2016 = allGrades[allGrades.Year == 2016]

#Then the 2013 data:
scores2013 = allGrades[allGrades.Year == 2013]

#Merge the data into a single dataFrame, lining up rows with similar districts:
byDistrict = pd.merge(scores2013, scores2016, how = 'left', on = 'district')
print(byDistrict)

byDistrict["difference"] = byDistrict.apply(makeDifferenceColumn, axis=1)
print(byDistrict)


#Create a map:
schoolMap = folium.Map(location=[40.75, -74.125])

#Create a layer, shaded by test scores:
schoolMap.choropleth(geo_path="schoolDistricts.json",
                     fill_color='YlGn', fill_opacity=0.5, line_opacity=0.5,
                     #threshold_scale = [100,200,300,400],
                     data = byDistrict,
                     key_on='feature.properties.SchoolDist',
                     columns = ['district', 'difference']
                     ) 
#Output the map to an .html file:
schoolMap.save(outfile='diffScores.html')
