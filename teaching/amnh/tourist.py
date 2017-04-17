# Lab 13: Manhattan Tourist Problem (from textbook)
# RGGS 670:  Algorithmic Approaches to Biological Data
# Spring 2016

import numpy as np

#The number of landmarks going east and south from a location:
east = np.array( [[3,2,4,0],[3,2,4,2],[0,7,3,4],[3,3,0,2],[1,3,2,2]] )
south = np.array( [[1,0,2,4,3],[4,6,5,2,1],[4,4,5,2,1],[5,6,8,5,3]] )

#Variables/constants used to keep track of the best path and trace it back:
size = 5
best = np.zeros( (size,size) )
traceback = np.zeros( (size,size) )
UP = 1
LEFT = -1

#Check to make sure this matches figure
print "east:", east
print "south:", south

#Set up first row and first column to gap:
best[0,0] = 0
for i in range(1,size):
     best[0,i] = best[0,i-1] + east[0,i-1]
     best[i,0] = best[i-1,0] + south[i-1,0]
     traceback[i,0] = UP
     traceback[0,i] = LEFT

print traceback

#Fill in the rest of the array:
for i in range(1,size):
     for j in range(1,size):
          best[i,j] = max(best[i,j-1] + east[i,j-1], best[i-1,j] + south[i-1,j])
          if best[i,j-1] + east[i,j-1] > best[i-1,j] + south[i-1,j]:
               traceback[i,j] = LEFT
          else:
               traceback[i,j] = UP

print best
print traceback


#Create the path working backwards from the lower right corner:
path = ""
i = size-1
j = size-1
while i > 0 or j > 0:
     if traceback[i,j] == UP:
          path = "south " + path
          i = i - 1
     else:
          path = "east " + path
          j = j -1

print "path:", path
