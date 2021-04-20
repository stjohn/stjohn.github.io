#3D plot of gradient descent puzzle (class work)
#Data Science, Lehman College, Spring 2016

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D #3D plotting
from matplotlib import cm               #Color maps
import numpy as np

#Create a figure:
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

#Set up the X, Y, and Z arrays:
X = np.arange(-2., 2., 0.01)
Y = np.arange(-2., 2., 0.01)
X, Y = np.meshgrid(X, Y)
#There are two minima for this surface:
#    Change the ranges and grid size to see more detail:
Z = (X**2 - 1)**2 + (X**2*Y - X - 1)**2

#Create and show the surface:
surf = ax.plot_surface(X, Y, Z,cmap=cm.BuPu)
fig.show()
