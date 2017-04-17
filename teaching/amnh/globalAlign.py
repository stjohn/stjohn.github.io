# Lab 13: Global Alignment (Needleman-Wunsch)
# RGGS 670:  Algorithmic Approaches to Biological Data
# Spring 2016


import numpy as np

#Some test sequences:
seq1 = "TATATAGG"
seq2 = "TAGAG"

size1 = len(seq1)+1
size2 = len(seq2)+1
best = np.zeros( (size1,size2) )
traceback = np.zeros( (size1,size2) )

UP = 1
LEFT = -1
DIAG = 2

delta = 1

def sigma(x,y):
     if x == y:
          return 1
     else:
          return -1

#Set up first row and first column to gap:
best[0,0] = 0
for i in range(1,size1):
     best[i,0] = best[i-1,0] - delta
     traceback[i,0] = UP

for i in range(1,size2):
     best[0,i] = best[0,i-1] - delta
     traceback[0,i] = LEFT

print best
print traceback

#Fill in the rest of the array:
for i in range(1,size1):
     for j in range(1,size2):
          best[i,j] = max(best[i,j-1] - delta, \
                          best[i-1,j] - delta, \
                          best[i-1,j-1] + sigma(seq1[i-1],seq2[j-1]))
          if best[i-1,j-1] + sigma(seq1[i-1],seq2[j-1]) == best[i,j]:
               traceback[i,j] = DIAG
          elif best[i-1,j] - delta == best[i,j]:
               traceback[i,j] = UP
          else:
               traceback[i,j] = LEFT
print "best: ", best
print "traceback: ", traceback

path1 = ""
path2 = ""
i = size1-1
j = size2-1
while i > 0 or j > 0:
     if traceback[i,j] == UP:
          path1 = seq1[i-1] + path1
          path2 = "-" + path2
          i = i - 1
     elif traceback[i,j] == LEFT:
          path1 = "-" + path1
          path2 = seq2[j-1] + path2
          j = j -1
     else:
          path1 = seq1[i-1] + path1
          path2 = seq2[j-1] + path2
          i -= 1
          j -= 1

print "An alignment is:"
print path1
print path2
