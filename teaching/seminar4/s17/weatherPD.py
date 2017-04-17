#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  6 17:05:13 2017

@author: stjohn

Uses multiple files from weather underground to graph
    historical max temperatures.
"""


#The libraries to plot, load webpages, and use regular expressions
import re
import requests
import pandas as pd

#A function that takes a URL and returns the temperature readings from that page:
def getTempFromWeb(url):
    data = requests.get(url)
    m = data.text.find("Min Temp")
    searchMin = re.search('\d+', data.text[m:])
    M = data.text.find("Max Temp")
    searchMax = re.search('\d+', data.text[M:])     
    return(int(searchMin.group(0)), int(searchMax.group(0)))


def main():
    #A dataFrame to hold the temperatures culled from the webpages:
    temps = pd.DataFrame(columns = ('Year', 'Min', 'Max'))
     
    #The url is made up of the prefix, year, and suffix:
    prefix = "http://www.wunderground.com/history/airport/KLGA/"
    suffix = "/02/02/DailyHistory"
     
    #For each year, create the URL, get the temps, and add to end of dataFrame:
    for year in range(2000,2017):       #For each year
        url = prefix+str(year)+suffix   #Make the url
        m, M = getTempFromWeb(url)      #Call the function to extract temp       
        print(year, m, M)               
        temps.loc[len(temps)] = (year, m, M)   #Add to the end of the dataFrame

    #Let's print out the dataFrame to make sure the data is there:           
    print(temps)
    #Use pandas' plotting to graph the temperatures:
    temps.plot(x='Year')

main()
