#Include the random and turtle libraries
import random
import turtle

#Create a turtle
teddy = turtle.Turtle()

#Have a loop that repeats 25 times
for i in range(25):
     #Inside that loop,
     #Move forward 10 steps
     teddy.forward(10)
     #Turn a random amount
     teddy.right(random.randrange(360))
     
#Close window on mouse click
turtle.exitonclick()
