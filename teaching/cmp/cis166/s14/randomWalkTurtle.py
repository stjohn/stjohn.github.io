import turtle
from random import *

def main():
    walker = turtle.Turtle()

    for i in range(1000):
        angle = randrange(0,360)
        walker.right(angle)
        walker.forward(10)

main()
        
