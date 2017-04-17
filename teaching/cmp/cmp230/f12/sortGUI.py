#Fall 2012, Intro Programming Lab
#Lehman College, CUNY

from graphics import *
from random import *


def main():
    #holds list of numbers to be sorted:
    a = [0]*40   

    #our display window:
    w = GraphWin("Sorting Demo",300,300)
    w.setCoords(-10,10,400,400)

    #First display the selection sort (code from book):
    initializeList(a, 40)
    displayList(a,0,40,w)
    w.getMouse()
    selSort(a,w)

    w.getMouse()
    clearScreen(w)
    initializeList(a, 40)
    displayList(a,0,40,w)
    bubbleSort(a,w)

    #Next display the merger sort (code from book):
    clearScreen(w)
    initializeList(a, 40)
    displayList(a,0,40,w)
    mergeSort(a,0,40,w)    

    w.getMouse()
    w.close()




#Bubble sort from pseudocode:
def bubbleSort(lst,w):
    n = len(lst)
    for j in range(n-1):
        for i in range(n-1):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                drawBox(lst, i, w)
                drawBox(lst, i+1,w)
        time.sleep(.25)
    


#Selection sort function from the textbook, with the addition
#   of code to draw the change each time
def selSort(lst,w):
    n = len(lst)
    for bottom in range(n-1):
        mp = bottom
        for i in range(bottom+1,n):
            if lst[i] < lst[mp]:
                mp = i
        lst[bottom], lst[mp] = lst[mp], lst[bottom]
        drawBox(lst, bottom, w)
        drawBox(lst, mp, w)
        time.sleep(.25)


#Merge sort functions, rewritten to make graphics easier:
def merge(a, start1, start2, end):
    # merge sorted lists lst1 and lst2 into lst3
    # these indexes keep track of current position in each list
    i1 = i2 = i3 = 0
    n1 = start2-start1
    n2 = end-start2
    tmp = [0]*(end-start1)

    # Loop while both pieces have data
    while i1 < n1 and i2 < n2:
        if a[start1 + i1] < a[start2 + i2]:     # copy from lst1
            tmp[i3] = a[start1 + i1]     
            i1 = i1 + 1
        else:                       # copy from list2
            tmp[i3] = a[start2 + i2]     
            i2 = i2 + 1
        i3 = i3 + 1                 # item added to lst3

    # Here either lst1 or lst2 is done, One of the following loops will
    # execute to finish up the merge.
    
    # Copy remaining items (if any) from lst1
    while i1 < n1:
        tmp[i3] = a[start1 + i1]
        i1 = i1 + 1
        i3 = i3 + 1
    # Copy remaining items (if any) from lst2
    while i2 < n2:
        tmp[i3] = a[start2+i2]
        i2 = i2 + 1
        i3 = i3 + 1
    for i in range(end-start1):
        a[start1+i] = tmp[i]

def mergeSort(a, start, stop, w):
    # Put items of lst in ascending order
    n = stop-start
    # Do nothing is lst contains 0 or 1 items
    if n > 1:
        # split into two sublists
        m = n // 2
        # recursively sort each piece
        mergeSort(a, start, start+m, w)
        mergeSort(a, start+m, stop, w)
        l1 = Line(Point(start*10,0), Point(start*10,400))
        l2 = Line(Point((stop+1)*10,0), Point((stop+1)*10,400))
        l1.setFill("green")
        l2.setFill("red")
        l1.draw(w)
        l2.draw(w)
        # merge the sorted pieces
        merge(a, start, start+m, stop)

        #update graphics:
        displayList(a,start, stop, w)
        time.sleep(1)
        l1.setFill("white")
        l2.setFill("white")

#White out the window, so, we can start again:
def clearScreen(w):
    r = Rectangle(Point(-10,10),Point(400,400))
    r.setFill("white")
    r.draw(w)


#Set up the initial list to have 40 random numbers:
def initializeList(a,n):
    for i in range(n):
        a[i] = 400*random()

#Draw a single box to the screen:
def drawBox(a,i,w):
    temp = Rectangle(Point(i*10, -10), Point((i+1)*10, 400))
    temp.setFill("white")
    temp.setOutline("white")
    temp.draw(w)

    temp = Rectangle(Point(i*10, 0), Point((i+1)*10, a[i]))
    temp.setFill("blue")
    temp.setOutline("white")
    temp.draw(w)


#draw the portion of the list from start to stop:
def displayList(a,start,stop,w): 
    for i in range(start,stop):        
        drawBox(a,i,w)
    
    

main()
