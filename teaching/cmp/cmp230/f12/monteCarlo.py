#Monte Carlo Simulation for stock prices
#Lab 10, Lehman College, CUNY, Fall 2012

from graphics import *
from random import *

def main():
    w = GraphWin("Stock Price Simulation", 400,200)
    w.setCoords(-10,-100,365,100)
    endingValue = [0]*10
    

    p = eval(input("Please enter a number between 0 and 1:"))

    #draw axis:
    Line(Point(0,0),Point(365,0)).draw(w)
    Line(Point(0,-100),Point(0,100)).draw(w)

    for i in range(10):
        endingValue[i] = monteCarlo(p,w)

    print("The ending values of our simulation were:", endingValue)
    print("Most money made was:", max(endingValue))
    print("Least money made was:", min(endingValue))

    w.getMouse()
    w.close()

def monteCarlo(prob, win):

    #we'll draw a line from the old point to the new point, starting at (0,0):
    oldPt = Point(0,0)
    money = 1
    

    for day in range(365):
        if (random() < prob):
            money = money + 1
        else:
            money = money - 1
        newPt = Point(day,money)
        Line(oldPt, newPt).draw(win)
        oldPt = newPt

    #Return the price of the stock on the last day:
    return(oldPt.getY())        

main()

    
