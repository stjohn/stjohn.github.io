#Fall 2012, Intro Programming Lab
#Lehman College, CUNY

from graphics import *
from random import *

def main():
    w = GraphWin("Spiral Demo",600,600)
    w.setCoords(-100,-100,100,100)
    
    #for i in range(0,100,4):
     #   Line(Point(-i,i), Point(i,i)).draw(w)
      #  Line(Point(i,-i), Point(i,i)).draw(w)
       # Line(Point(-i,-i), Point(i,-i)).draw(w)
        #Line(Point(-i,-i), Point(-i,i+1)).draw(w)

    oldPoint = Point(1,1)
    up = 1
    right = 1
    for l in range(1000):
        newPoint = Point(1.01*right*oldPoint.getX()+1,1.01*up*oldPoint.getY()+10)
        Line(oldPoint,newPoint).draw(w)
        oldPoint = newPoint
        up = (-1)**l
        right = (-1)**(l+1)

        
    w.getMouse()
    w.getClose()
main()
    
