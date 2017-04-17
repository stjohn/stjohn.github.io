#Idea from:  http://www.motionscript.com/mastering-expressions/simulation-basics-1.html

from turtle import *
from math import *

def main():
    veloc = .5  #horizontal velocity (pixels per second)
    amp = 75    #sine wave amplitude (pixels)
    freq = .01  #oscillations per second

    #Set up a graphics window and turtle:
    win = Screen()
    ball = Turtle()
    ball.speed(10)
    win.setworldcoordinates(0.0, -100.0, 500.0, 100.0)

    #Draw a line for the x-axis:
    ball.up()
    goto(0,0)
    ball.down()
    ball.forward(500)
    ball.up()
    ball.backward(500)
    ball.down()

    #Draw a ball that follows a sine wave
    for time in range(500):
        #For each time step, move the turtle to (time, sin(time))
        #       (with some scaling to make it fill screen)
        ball.goto(time,int(amp*sin(freq*time*2*pi)))        

    win.exitonclick()         #Close the window when clicked
    
main()
