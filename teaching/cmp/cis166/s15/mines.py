from turtle import *
from random import *

""" Sets up the screen with the origin in upper left corner """
def setUpScreen(xMax,yMax):
    win = Screen()
    win.setworldcoordinates(-0.5, yMax+0.5,xMax+0.5,-0.5)
    return win


""" Draws a grid to the graphics window"""
def drawGrid(xMax,yMax):
    tic = Turtle()
    tic.speed(10)
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

def createMines(numMines, side):
    grid = [[""]*side]*side
    n = 0
    while n < numMines:
        #Generate a new mine:
        x = randrange(side)
        y = randrange(side)
        if grid[x][y] == "":
            grid[x][y] = "X"
            n = n + 1
    return grid

def main():
    side=10
    numMines = 40
    foundMines = 0
    squaresLeft = side*side
    exploded = 0
    
    setUpScreen(side,side)
    drawGrid(side,side)
    grid = createMines(numMines,side)

    while foundMines < numMines:
        x,y = eval(input('Enter x,y (separated by comma): '))
        kind = input('Type "M" for mine (anything else for empty cell):')
        if grid[x][y] == "X":
            foundMines = foundMines + 1
            if kind == "M" or kind == "m":
                print("You found a mine!")
                
            
main()
        
        
        
    
