# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 04:32:09 2016

@author: stjohn
"""

import turtle

#Parsing newick format:
t = "((Ape,Baboon), Chimp)"
adjT = {}
#Add in a root:
adjT["root"] = ("", [])
iNodeCount = 0


def printTree(s):
    tess = Turtle.turtle()
    level = 0
    for c in s:
        if c == '(':
            level += 1
            tess.left(45)
            tess.forward(1000/level)
            tess.right(45)
        elif c == ',':
            tess.right(135)
            tess.forward(1000/level)
            tess.left(90)
            tess.forward(1000/level)
            tess.left(45)
        elif c == ')':
            tess.left(135)
            tess.forward(1000/level)
            tess.left(135)
            level = level-1
        else:   #c is a letter
            tess.write(c)
                

