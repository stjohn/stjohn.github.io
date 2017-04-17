# Spring 2014, CMP230, Lab 11 and CIS 166, Lab 14
# This is a modified version of sortGUI.py which is available
# on http://comet.lehman.cuny.edu/sfakhouri/teaching/cmp/cmp230/f12/sortGUI.py~
# Modifications are made by Maryam Ghaffari Saadat

from graphics import *
from random import *

n = 10

def main():
    #holds list of numbers to be sorted:
    a = [0]*n 

    #our display window:
    w = GraphWin("Sorting Demo",500,500)
    w.setCoords(-5,0,n*10,n*10)

    #First, display the selection sort (code from book):
    initializeList(a)
    displayList(a,w)
    selSort(a,w)

    #Next, display the bubble sort
    clearScreen(w)
    initializeList(a)
    displayList(a,w)
    bubbleSort(a,w)

    w.getMouse()
    w.close()


#Selection sort function from the textbook, with the addition
#   of code to draw the change each time
def selSort(lst,w):
    n = len(lst)
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1,n):
            if lst[i] < lst[mp]:
                mp = i
        if mp != bottom:
            # draw the bars that are to be swapped
            drawMovingBars(lst, bottom, mp, w)
            # swap the bars
            lst[bottom], lst[mp] = lst[mp], lst[bottom]
            # draw the bars after they are swapped
            drawMovingBars(lst, bottom, mp, w)

#Bubble sort from pseudocode:
def bubbleSort(lst,w):
    #n = len(lst)
    for j in range(n-1):
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                # draw the bars that are to be swapped            
                drawMovingBars(lst, i, i+1, w)
                # swap the bars
                lst[i], lst[i+1] = lst[i+1], lst[i]
                # draw the bars after they are swapped
                drawMovingBars(lst, i, i+1, w)
    

#Set up the initial list to have 40 random numbers:
def initializeList(a):
    for i in range(n):
        a[i] = (n-1)*10*random()+10

def drawMovingBars(lst, box_1_index, box_2_index, w):
    # draw the boxes that are moving, with red outlines 
    drawBox(lst, box_1_index, w, True)
    drawBox(lst, box_2_index, w, True)

    # get a mouse click
    w.getMouse()

    ## uncomment to: wait for .2 seconds (= 2 deciseconds)
    #time.sleep(.2)

    # redraw the boxes without red outlines 
    drawBox(lst, box_1_index, w, False)
    drawBox(lst, box_2_index, w, False)    


#Draw a single box to the screen:
def drawBox(a,i,w, isMoving):
    # clear the space for bar i
    barSpace = Rectangle(Point(i*10, 0), Point((i+1)*10, n*10))
    barSpace.setFill("white")
    barSpace.setOutline("white")
    barSpace.draw(w)

    # create a new bar with hight of a[i] 
    bar = Rectangle(Point(i*10, 0), Point((i+1)*10, a[i]))
    # set the colour of the bar to be a shade of blue
    # the taller the bar, the lighter the blue.
    bar.setFill(color_rgb(0,0,a[i]*(255/(n*10))))
    
    # set the thickness of the outline of the bar to 3 pixels
    bar.setWidth(3)

    # if the bar is moving, set the outline colour to red 
    if isMoving:
        bar.setOutline('red')
    # otherwise set the outline colour to white
    else:
        bar.setOutline("white")

    # draw the bar
    bar.draw(w)


#draw the portion of the list from start to stop:
def displayList(a,w): 
    for i in range(len(a)):        
        drawBox(a,i,w,False)
    
#White out the window, so, we can start again:
def clearScreen(w):
    r = Rectangle(Point(0,0),Point(n*10,n*10))
    r.setFill("white")
    r.draw(w)    

main()
