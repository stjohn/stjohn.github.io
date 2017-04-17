import turtle

def tree(branchLen,t):
    
    if branchLen > 5:
        t.forward(branchLen)
        t.right(20)
        tree(branchLen-10,t)
        t.left(40)
        tree(branchLen-10,t)
        t.right(20)
        if branchLen < 10:
            t.color("green")
            t.backward(branchLen)
            t.color("brown")
        else:
            t.backward(branchLen)

def main():
    #Set up a turtle:
    t = turtle.Turtle()
    
    #Set up the drawing window:
    myWin = turtle.Screen()

    #Turn the turtle 90 degrees to the left:
    t.left(90)

    #Lift up the drawing pen and move 150 steps:
    t.up()
    t.backward(250)

    #Put the drawing pen back and change the color to green:
    t.down()
    t.color("brown")

    #Draw a tree with initial branch length 100:
    tree(100,t)

    #Close the drawing window when clicked:
    myWin.exitonclick()

main()
