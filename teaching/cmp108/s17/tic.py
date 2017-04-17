#Data Analysis, Spring 2017
#Lehman College, City University of New York
#First Version of Tic-Tac-Toe
#   This version does NO checking of anything (it doesn't 
#   check who wins, doesn't check for legal entries, etc).
#   We will add that later in the semester

import turtle


#Set up the screen and turtle
win = turtle.Screen()
tic = turtle.Turtle()
tic.speed(10)
#Change the coordinates to make it easier to translate moves to screen coordinates:
win.setworldcoordinates(-0.5,-0.5,3.5, 3.5)

#Draw the horizontal bars of the game board:
for i in range(1,3):
   tic.penup()
   tic.goto(0,i)
   tic.pendown()
   tic.forward(3)

#Draw the vertical bars of the game board:
tic.left(90)    #Point the turtle in the right direction before drawing
for i in range(1,3):
   tic.penup()
   tic.goto(i,0)
   tic.pendown()
   tic.forward(3)

tic.penup()        #Don't need to draw any more lines, so, keep pen up
       

#Ask the user for the moves, alternating between the players X and O:
for i in range(4):
   x = int(input("Enter x coordinate for X's move: "))
   y = int(input("Enter y coordinate for X's move: "))
   tic.goto(x+.25,y+.25)
   tic.write("X",font=('Arial', 90, 'normal'))
   x = int(input("Enter x coordinate for O's move: "))
   y = int(input("Enter y coordinate for O's move: ")) 
   tic.goto(x+.25,y+.25)
   tic.write("O",font=('Arial', 90, 'normal'))

#Display an ending message: 
tic.goto(-0.25,-0.25)
tic.write("Thank you for playing!",font=('Arial', 20, 'normal'))
   
win.exitonclick()#Closes the graphics window when mouse is clicked

