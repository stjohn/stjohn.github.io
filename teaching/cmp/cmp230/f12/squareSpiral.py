#From http://interactivepython.org/courselib/static/pythonds/Recursion/graphical.html

import turtle

#This function draws a line, turns right, and calls itself
#  to draw a shorter line:
def drawSpiral(t,lineLength):
    if lineLength > 0:
        t.forward(lineLength)
        t.right(90)
        drawSpiral(t, lineLength-5)

def main():
    #Set up a turtle:
    myTurtle = turtle.Turtle()

    #Set up a graphics window:
    myWin = turtle.Screen()

    #Call the function that will draw a spiral
    drawSpiral(myTurtle,150)

    #After mouse click, close window
    myWin.exitonclick()

main()
