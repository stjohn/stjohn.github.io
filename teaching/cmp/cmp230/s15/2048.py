"""
Katherine St. John, Spring 2015
Introductory Programming, Lehman College, CUNY
A summing game based on 2048
by Gabriele Cirulli (http://gabrielecirulli.github.io/2048/)
"""

from turtle import *
from random import *

""" Welcome messages for the program"""
def welcome():
    print("Welcome to a summing game")
    print("For each move pick a direction")
    print("([L]eft, [R]ight, [U]p, or [D]own).")    
    print()

""" Sets up the screen with the origin in upper left corner """
def setUp(xMax,yMax):
    win = Screen()
    win.setworldcoordinates(-0.5, yMax+0.5,xMax+0.5,-0.5)
    t = Turtle()
    t.speed(10)
    t.hideturtle()
    return win,t

""" Draws a grid to the graphics window"""
def drawGrid(tic,xMax,yMax):
    #Draw the vertical bars of the game board:
    for i in range(0,xMax+1):
        tic.up()
        tic.goto(0,i)
        tic.down()
        tic.forward(yMax)
    #Draw the horizontal bars of the game board:
    tic.left(90)    #Point the turtle in the right direction before drawing
    for i in range(0,yMax+1):
        tic.up()
        tic.goto(i,0)
        tic.down()
        tic.forward(xMax)

""" Fills in the square (x,y) and write value"""
def fillSquareWithValue(t,x,y,value):
    t.up()
    t.goto(x+.1,y+.1)
    t.fillcolor("white")
    t.begin_fill()
    for i in range(4):
        t.forward(.8)
        t.right(90)
    t.end_fill()
    t.goto(x+.50,y+.85)
    t.write(value,align="center",font=('Arial', 70, 'normal'))    

def drawBoard(t,grid):
    for i in range(4):
        for j in range(4):
            fillSquareWithValue(t,i,j,grid[i][j])

def generateNewSquare(t,grid):
    x = randrange(4)
    y = randrange(4)
    while grid[x][y] != "":
        x = randrange(4)
        y = randrange(4)
    grid[x][y] = "2"
    fillSquareWithValue(t,x,y,"2")

def slideGridDown(grid):
    for i in range(4):
        for j in range(3,0,-1):
            if grid[i][j] == "" and grid[i][j-1] != "":
                grid[i][j] = grid[i][j-1]
                grid[i][j-1] = ""


def slideGridUp(grid):
    for i in range(4):
        for j in range(3):
            if grid[i][j] == "" and grid[i][j+1] != "":
                grid[i][j] = grid[i][j+1]
                grid[i][j+1] = ""


def combineRows(grid,source,target):
    for i in range(4):
        if grid[i][target] != "" and grid[i][target] == grid[i][source]:
            grid[i][target] = str(int(grid[i][target])+int(grid[i][source]))
            grid[i][source] = ""
           

def slideGridRight(grid):
    for j in range(4):
        for i in range(3,0,-1):
            if grid[i][j] == "" and grid[i-1][j] != "":
                grid[i][j] = grid[i-1][j]
                grid[i-1][j] = ""


def slideGridLeft(grid):
    for j in range(4):
        for i in range(3):
            if grid[i][j] == "" and grid[i+1][j] != "":
                grid[i][j] = grid[i+1][j]
                grid[i+1][j] = ""


def combineColumns(grid,source,target):
    for i in range(4):
        if grid[target][i] != "" and grid[target][i] == grid[source][i]:
            grid[target][i] = str(int(grid[target][i])+int(grid[source][i]))
            grid[source][i] = ""
           
                
def moveLeft(grid):
    score = 0
    for i in range(3):
        slideGridLeft(grid)
    for i in range(3):
        combineColumns(grid,i+1,i)
    slideGridLeft(grid)   


def moveRight(grid):
    score = 0
    for i in range(3):
        slideGridRight(grid)
    for i in range(3,0,-1):
        combineColumns(grid,i-1,i)
    slideGridRight(grid)     


def moveUp(grid):
    for i in range(3):
        slideGridUp(grid)
    for i in range(3):
        combineRows(grid,i+1,i)
    slideGridUp(grid)     

def moveDown(grid):
    for i in range(3):
        slideGridDown(grid)
    for i in range(3,0,-1):
        combineRows(grid,i-1,i)
    slideGridDown(grid) 
    
"""Asks user for move, makes move and returns the number of squares freed"""
def makeMove(t,grid):
    move = input("Enter move([L]eft, [R]ight, [U]p, or [D]own):")
    if move == "L" or move == "l":
        moveLeft(grid)
    if move == "R" or move == "r":
        moveRight(grid)
    if move == "U" or move == "u":
        moveUp(grid)
    if move == "D" or move == "d":
        moveDown(grid)
    drawBoard(t,grid)

"""Return the number of squares that are filled"""
def squaresFilled(grid):
    filled = 0
    for i in range(4):
        for j in range(4):
            if grid[i][j] != "":
                filled = filled + 1
    return(filled)

""" Write thank you message and close window on click"""
def conclusion(win,t):
    t.up()
    t.goto(2,4.25)
    t.write("Thank you for playing!",align="center",font=('Arial', 20, 'normal'))    

    win.exitonclick()


         
def main():
    grid = [["","","",""],["","","",""],["","","",""],["","","",""]]    
    welcome()
    win,t = setUp(4,4)
    drawGrid(t,4,4)     

    while squaresFilled(grid) < 16: #While there are empty squares, keep playing:
        generateNewSquare(t,grid)
        makeMove(t,grid)

    conclusion(win,t)    
    
main()
