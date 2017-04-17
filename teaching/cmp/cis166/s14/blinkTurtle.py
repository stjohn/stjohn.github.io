#Blinking turtle for introductory programming lab

import turtle

def main():
    numSides = 8
    daniel = turtle.Turtle()    #Set up a turtle named "daniel"
    myWin = turtle.Screen()     #The graphics window

    #Draw a square
    for i in range(numSides):
        if i % 2 == 0:
            daniel.color("red")
        else:
            daniel.color("green")        
        daniel.forward(100)     #Move forward 10 steps
        daniel.right(360/numSides)  #Turn 90 degrees to the right

    myWin.exitonclick()         #Close the window when clicked
    
main()		
