import turtle
from random import *

#A function that sets up the x-axis on the screen:
def setUpScreen():
    #Create a turtle to draw the x-axis
    t = turtle.Turtle()
    t.speed(0)
    #Lift it's pen up and move it to the far left
    t.up()
    t.right(180)
    t.forward(350)
    #Draw the axis
    t.down()
    t.right(180)
    t.forward(700)

#Sets up num turtles to all start at the far left,
#   to tell them apart, color them different shades of green
def setUpTurtles(num):    
    turtleList = []             #Our list of turtles
    for i in range(num):
        t = turtle.Turtle()
        t.speed(0)              #Fastest turtle speed to avoid boredom
        t.up()
        t.right(180)
        t.forward(350)
        t.right(180)
        t.down()
        #Choose random values for the red, green, and blue (RGB):
        t.color(random(), random(), random())
        turtleList.append(t)

    return(turtleList)


def simulate(turtleList, prob, money, time):
    #Calculate and graph amount money made over 90 days
    for day in range(time):
        for i in range(len(turtleList)):
            #If the random number is below the turtle's prob, go up
            if (random() < prob[i]):
                money[i] = money[i] + 1
                turtleList[i].left(45)
                turtleList[i].forward(10)
                turtleList[i].right(45)
            #Else, go down
            else:
                money[i] = money[i] - 1
                turtleList[i].right(45)
                turtleList[i].forward(10)
                turtleList[i].left(45)


def main():
    #Keep track of the money made by each turtle/chain:
    money = [0]*10
    prob = [0]*10

    #Set up screen and turtles
    setUpScreen()
    turtleList = setUpTurtles(10)
    for i in range(10):
        prob[i] = random()
        print(prob[i])

    #Simulate the money gained and lost for each stock over 90 days:
    simulate(turtleList, prob, money, 90)

    print(money)
    print("Max money made is", max(money))
    print("Min money made is", min(money))

    turtle.Screen().exitonclick()

main()
