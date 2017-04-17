import turtle


def petal(t):
    t.forward(100)
    t.right(45)
    t.forward(20)
    t.right(120)
    t.forward(20)
    t.right(35)
    t.forward(100)


def main():
    flower = turtle.Turtle()    #Set up a turtle named "flower"
    flower.color("purple")
    myWin = turtle.Screen()

    #for i in range(19):
    petal(flower)
     #   flower.left(19.5)

main()
