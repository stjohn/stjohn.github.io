# Mystery point game for Lab 9
# Lehman College, CUNY, Fall 2012

from graphics import *
from math import *
from random import *

# Reuse the distance function we wrote for Lab 8:
def dist(p1,p2):
    dist = sqrt((p1.getX()-p2.getX())**2 + (p1.getY() - p2.getY())**2)
    return dist


def main():
    w = GraphWin("Target Practice",500,500)
    w.setCoords(-250,-250,250,250)

    #Generate a mystery point (at a random location):
    x = randrange(-200,200)
    y = randrange(-200,200)
    print("x and y are:",x,y)
    mysteryPoint = Point(x,y)

    #Text to tell the user what's happening:
    t = Text(Point(0,-210), "Click on the mystery point")
    t.setSize(16)
    t.draw(w)

    #Get the point:
    p = w.getMouse()
    p.draw(w)
    d = dist(mysteryPoint, p)
    print("distance from mystery point is:", d)

    t2 = Text(Point(0,-230), "")
    t2.setSize(16)
    t2.draw(w)

    #Keep going until they click close to the point:
    while d > 20:
        if p.getX() < mysteryPoint.getX():
            t.setText("Click again! You were too far left")
        else:
            t.setText("Click again! You were too far right")
        if p.getY() < mysteryPoint.getY():
            t2.setText("Click again! You were too low")
        else:
            t2.setText("Click again! You were too high")    
        p = w.getMouse()
        p.draw(w)
        d = dist(mysteryPoint, p)
        print("distance from mystery point is:", d)

    t.setText("Congratulations!  You found the mystery point!")

    #keep the window up until the user clicks
    w.getMouse()
    w.close()

main()






