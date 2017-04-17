#Demonstrating linear transformations to images
#Data Science, Lehman College, Spring 2016

import matplotlib.pyplot as plt
import numpy as np


#Original image:
img = plt.imread("Midwest_Flooding_01012016_sm.png")
plt.imshow(img)
plt.show()


#Make a new image, rotated by theta and stretched by stretch:
ht = 2*img.shape[0]
wd = 2*img.shape[1]
r = np.ones((ht,wd,3))
theta = -np.pi/8
rotate = np.array([[np.cos(theta),-np.sin(theta)],[np.sin(theta),np.cos(theta)]])
stretch = np.array([[0.5,0],[0,2]])

for i in range(img.shape[0]):
     for j in range(img.shape[1]):
          (newI,newJ)= rotate.dot(stretch.dot((i,j)))
          newI,newJ = int(newI),int(newJ)
          if 0 < newI < r.shape[0] and 0 < newJ < r.shape[1]:
               r[int(newI),int(newJ),:] = img[i,j,:]

plt.imshow(r)
plt.show()
