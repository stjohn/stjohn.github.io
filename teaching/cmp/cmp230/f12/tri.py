import turtle

def triangle(t, l):
    if l > 10:
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.left(120)
        t.forward(l)
        t.backward(l/2)
        t.left(60)
        triangle(t,l/2)

def main():
    #Set up a turtle:
    t = turtle.Turtle()
    
    #Set up the drawing window:
    myWin = turtle.Screen()

    t.up()
    t.backward(100)
    t.down()
    #Draw a tree with initial branch length 100:
    triangle(t,300)

    #Close the drawing window when clicked:
    myWin.exitonclick()

main()
