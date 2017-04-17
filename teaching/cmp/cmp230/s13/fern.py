import turtle

def fern(turtle, size):
    if size > 4:
        turtle.forward(size/25)
        turtle.left(90)
        fern(turtle, size*0.3)
        turtle.right(180)
        fern(turtle, size*0.3)
        turtle.left(90)
        fern(turtle, size*0.85)
        turtle.backward(size/25)

def main():
    t = turtle.Turtle()
    t.speed(0)
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    fern(t, 500)

main()
