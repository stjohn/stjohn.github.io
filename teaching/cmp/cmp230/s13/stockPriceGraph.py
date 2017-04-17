# Graphing historical stock data
from graphics import *

def main():
    fileName = input("Enter file name: ")
    inFile = open(fileName, "r")
    lines = inFile.readlines()

    s = "Chart of " + fileName
    w = GraphWin(fileName)
    w.setCoords(-10,-10,270,1000)

    for i in range(1,len(lines)-1):
        words = lines[len(lines)-i].split(",")
        price = float(eval(words[1]))
        print(price)
        Point(i, price).draw(w)

main()

    
    
