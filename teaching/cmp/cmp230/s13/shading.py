#Changing colors:

from graphics import *

def main():
    w = GraphWin("Color Scale")
    w.setCoords(0,0,100,100)

    for i in range(100):
        r = Rectangle(Point(i,0), Point(i+1,100))
        c = color_rgb(0,0,55+2*i)
        r.setFill(c)
        r.setOutline(c)
        r.draw(w)

    w.getMouse()
    w.close()

main()


def main2():
    w = GraphWin("Color Scale")
    w.setCoords(-10,-150,150,150)

    for i in range(100):
        r = Circle(Point(i,0), .5*i)
        col = color_rgb(5+2.5*i,0,0)
        r.setFill(col)
        r.setOutline(col)
        r.draw(w)

    w.getMouse()
    w.close()

main2()

def main3():
    w = GraphWin("Color Scale")
    w.setCoords(-20,-20,120,120)

    for i in range(100):
        r = Circle(Point(i,i),10)
        col = color_rgb(0,55+2*i ,0)
        r.setFill(col)
        r.setOutline(col)
        r.draw(w)

    w.getMouse()
    w.close()

main3()
