import turtle

#Uses a file to store the colors
#First open up the file:
infile = open("colorShape")

#Create a turtle, named tortuga:
tortuga = turtle.Turtle()
tortuga.shape("turtle")

#For each line in our file, split it in parts, and draw a side that color and shape:
for line in infile:
	words = line.split(' ')
	tortuga.color(words[0])
	tortuga.shape(words[1])
	tortuga.forward(100)
	tortuga.left(93)
