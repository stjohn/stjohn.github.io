# Archery Program for Lab 8
# Lehman College, CUNY, Fall 2012

from graphics import *
from math import *

def dist(p1,p2):
    dist = sqrt((p1.getX()-p2.getX())**2 + (p1.getY() - p2.getY())**2)
    return dist

def main():
    w = GraphWin("Target Practice",500,500)
    w.setCoords(-250,-250,250,250)

    #make a point for the origin since we'll use it over and over again:
    origin = Point(0,0)

    #draw the target:
    for radius in range(10,0,-1):
        c = Circle(origin, 20*radius)
        if radius % 2 == 0:
            c.setFill("red")
        else:
            c.setFill("yellow")
        c.draw(w)

    #score the users click:
    t = Text(Point(0,-225), "Click on the target")
    t.setSize(20)
    t.draw(w)
    p = w.getMouse()
    d = dist(origin, p)

    #This line prints to the IDLE shell window, so, we can debug the program:
    print("You clicked on (", p.getX(), ",", p.getY(),") with distance: ", d)

    if d < 20:
        t.setText("Bullseye! 10 points")
    elif d < 200:
        t.setText("Hit the target! 1 point")
    else:
        t.setText("Missed! 0 points")
    
    #keep the window up until the user clicks
    w.getMouse()
    w.close()

main()
