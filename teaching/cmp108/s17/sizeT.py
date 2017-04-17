import turtle

#Uses a file to store the colors
#First open up the file:
infile = open("sizeList")
#Create a turtle, named tortuga:
tortuga = turtle.Turtle()
tortuga.shape("turtle")


#For each color in our file, draw a side that color and then turn 93 degrees:
for c in infile:
     tortuga.pensize(int(c))
     tortuga.forward(100)
     tortuga.left(93)
