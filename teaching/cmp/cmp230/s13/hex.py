import turtle

def main():
    daniel = turtle.Turtle()

    for i in range(6):
        daniel.forward(100)
        daniel.right(360/6)
        

    daniel.up()
    daniel.left(120)
    daniel.forward(100)
    daniel.down()

    for i in range(10):
        daniel.forward(100)
        daniel.right(360/10*3)

main()
