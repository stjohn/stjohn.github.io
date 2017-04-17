import turtle


def drawStem(t):
    t.color("green")
    t.down()
    t.right(90)
    t.forward(300)
    t.backward(300)
    t.left(90)
    

def drawPetal(t,s):
    t.color(s)
    t.forward(10)
    t.left(5)
    t.forward(100)
    t.right(25)
    t.forward(20)
    t.right(120)
    t.forward(20)
    t.right(25)
    t.forward(10)
    t.right(5)
    t.forward(100)


from turtle import *
def main():
	myWin = turtle.Screen()     	#The graphics window
	tess = turtle.Turtle()		#Tess will be our turtle for this program
	drawStem(tess)			#Draw a green stem 	
	for i in range(20):
		drawPetal(tess,"blue")	#Draws a blue petal for our flower
		drawPetal(tess,"purple")#Draws a purple petal for our flower
	myWin.exitonclick()         	#Close the window when clicked	

main()
