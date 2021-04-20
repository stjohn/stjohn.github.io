#Katherine St. John
#Data Science, Spring 2016
#Simple example of two different plots with different scales

import matplotlib.pyplot as plt
from random import random

#Create some random data to plot:
x = [i for i in range(1,32)]
y1 = [i + random() for i in range(1,32)]
y2 = [-i - random() for i in range(1,32)] 

#Set up a figure
fig = plt.figure()

#The first set of data plotted is blue:
ax1 = fig.add_subplot(111)
ax1.plot(x,y1,'b-')
ax1.set_ylabel("Density", color="b")
for tl in ax1.get_yticklabels():
    tl.set_color('b')

#The second set of data plotted is red:
ax2 = ax1.twinx()
ax2.plot(x,y2, 'ro')
ax2.set_ylabel("Other", color="r")
for tl in ax2.get_yticklabels():
    tl.set_color('r')

#Add in a title and show:
plt.title('Two different plots with different scales')
plt.show()
