import turtle

def nested(t, k):
     for i in range(3):
          t.left(120)
          t.forward(k)
     if k > 10:
          nested(t, k/2)


def nested2(t, k):
     for i in range(3):
          t.left(120)
          t.forward(k)
          if k > 10:
               nested2(t, k/2)

tess = turtle.Turtle()
tess.shape("turtle")
nested(tess,320)

tess.color("purple")
tess.up()
tess.goto(345,0)
tess.down()
nested2(tess, 320)

turtle.exitonclick()
