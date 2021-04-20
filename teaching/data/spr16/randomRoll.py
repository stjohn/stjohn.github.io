# A dice-rolling simulation that calculates observed
# and expected average sums
# Version 4:  prints sums to screen, turtles draw distribution,
#              and computes average and expectation
#              and prints out a plot using matplotlib

import random       #Module with random number generators
import turtle       #Module with turtle graphics
import matplotlib.pyplot   #Module with mathematical plotting tools

"""Sets up the window and list of turtles"""
def setUpTurtles(n,height):
     w = turtle.Screen()
     w.setworldcoordinates(-0.5,-1,n,height)
     turtles = []
     for i in range(n):
          teddy = turtle.Turtle()
          teddy.shape("turtle")
          teddy.up()
          teddy.goto(i,-1)
          teddy.write(str(i))
          teddy.goto(i,0)
          teddy.left(90)
          turtles.append(teddy)
     return w, turtles

"""Calculates the average of the observed sums"""
def calculateAverage(sums, numTrials):
     total = 0.0
     for i in range(len(sums)):
          total = total + i*sums[i]
     return total/numTrials

"""Using just the number of sides of the dice, calculates the expectation"""
def calculateExpectation(die1,die2):
     values = [0.0]*(die1+die2+2)
     total = 0.0
     for i in range(1,die1+1):
          for j in range(1,die2+1):
               values[i+j] += ((i+j)*(1.0/die1)*(1.0/die2))
     for k in range(len(values)):
          total = total + values[k]
     return total

def main():
     numSidesDie1 = 6         #Num sides of first die
     numSidesDie2 = 6         #Num sides of second die
     numTrials = 100          #Number of rolls
     width = numSidesDie1+numSidesDie2+1 #Highest sum possible
     sums = [0]*(width)       #A list for storing sums that were rolled
     height = numTrials/width*3    #Height of the graphics window
     w, turtles = setUpTurtles(width,height) #Set up window and turtle list

     #Loop repeats for each roll:
     for i in range(numTrials):
          #Roll each die and store sum in trial:
          trial = random.randrange(1,numSidesDie1+1) + random.randrange(1,numSidesDie2+1)
          #Update the number of times that sum has been seen:
          sums[trial] = sums[trial] + 1
          #Print the sums so far:
          print sums
          #Move corresponding turtle forward and stamp:
          turtles[trial].forward(1)
          turtles[trial].stamp()

     #Call functions to calculate average and expectation:
     ave = calculateAverage(sums,numTrials)
     exp = calculateExpectation(numSidesDie1, numSidesDie2)
     print "The average is", ave
     print "The expectation is", exp

     #Plot final data using matplotlib
     matplotlib.pyplot.plot(sums)
     matplotlib.pyplot.xlabel('sums')
     matplotlib.pyplot.ylabel('frequency')
     matplotlib.pyplot.show()
     
     w.exitonclick()     #Closes graphics window on mouse click:

main()        #Calls the main() function
