# Game of Life program for Lab 10
# Lehman College, CUNY Fall 2012

from graphics import *
from random import *

def main():
    w = GraphWin("Game of Life", 440,440)
    w.setCoords(-1,-1,21,21)

    #draw grid lines:
    for i in range(21):
        Line(Point(i,0), Point(i,20)).draw(w)
        Line(Point(0,i), Point(20,i)).draw(w)

    #set up the array to keep track of squares:
    a = createBoard(20)

    #display board:
    displayBoard(a, w)

    #update board
    updateBoard(a)

    w.getMouse()
    w.getClose()


def createBoard(size):
    board = [[0]*size for i in range(size)]
    for row in range(size):
        for col in range(size):
            if randrange(4) == 1:
                board[row][col] = 1
    return board


def displayBoard(a,w):
    for row in range(len(a)):
        for col in range(len(a[row])):
            if a[row][col] == 1:
                print(row, col)
                r = Rectangle(Point(row,col), Point(row+1,col+1))
                r.setFill("green")
                r.draw(w)
            else:
                r = Rectangle(Point(row,col), Point(row+1,col+1))
                r.setFill("blue")
                r.draw(w)

def countNeighbors(a, row, col):
    count = 0
    return count

def updateBoard(a):
    for row in range(len(a)):
        for col in range(len(a[row])):
            if countNeigbhors(a, row, col) < 2:
               a[row][col] = 0 
            #else:
                
            


main()
