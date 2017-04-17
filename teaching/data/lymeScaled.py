#Katherine St. John
#Data Science, Spring 2016
#Simple example of scaling vectors using list comprehensions

import matplotlib.pyplot as plt

#Data from CDC's Lyme Disease page:
years = [2003,2004,2005,2006,2007,2008,2009,2010,2011]
ny = [5399,5100,5565,4460,4165,5741,4134,2385,3118]
nj = [2887,2698,3363,2432,3134,3214,4598,3320,3398]
ct = [1403,1348,1810,1788,3058,2738,2751,1964,2004]

#We'll do the same operations for each state, so put in a function:
def scale(stateList, plt, lab,col):
     """
     Takes a list, label, and color and creates a scatter plot
     of the percentage change with respect to the first entry
     in the list.
     """
     baseNum = stateList[0]
     scaled= [i*100/baseNum-100 for i in stateList]
     plt.scatter(years, scaled, label=lab, c = col, s=75)


#Create scatter plots for each state:
scale(ny,plt,"NY", "blue")
scale(nj,plt,"NJ", "red")
scale(ct,plt,"CT", "purple")

#Set up title, axis labels, and legend, and then show:
plt.title("Lyme Disease in NY, NJ, & CT")
plt.xlabel('Years')
plt.ylabel('Percent Change')
plt.legend()
plt.show()


