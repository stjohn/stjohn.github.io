import turtle

def main():
    daniel = turtle.Turtle()    #Set up a turtle named "daniel"
    myWin = turtle.Screen()     #The graphics window
        
    daniel.up()
    daniel.left(120)
    daniel.forward(170)
    daniel.down()

    for i in range(10):
        daniel.forward(100)
        daniel.right(360/10*3)

    daniel.up()
    daniel.right(105)
    daniel.forward(160)
    daniel.down()

    for i in range(15):
        daniel.forward(100)
        daniel.right(192)

    daniel.up()
    daniel.right(120)
    daniel.forward(250)
    daniel.down()

    for i in range(100):
        daniel.forward(i)
        daniel.right(91)
    myWin.exitonclick()

main()
