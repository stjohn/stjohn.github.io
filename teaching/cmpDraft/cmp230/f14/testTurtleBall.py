#Test program for turtles as billard balls
import turtle
from turtleBall import *
from random import *

def setUpTable(xMin,yMin,side):
    draw = turtle.Turtle()
    draw.up()
    draw.goto(xMin,yMin)
    draw.down()
    for i in range(4):
        draw.forward(side)
        draw.left(90)
    draw.hideturtle()
    

def main():
    setUpTable(-200,-200,400)
    b1 = TurtleBall("blue",random()*360,-200,-200,200,200)
    b1.move(400)
    
    turtle.Screen().exitonclick()
    
main()
