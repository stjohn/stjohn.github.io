#Introductory Programming, Lehman College, CUNY
#Spring 2015
#A template file for drawing earthquake data to the screen
#Already written: functions that
#         setup the screen, and
#         draw ocean boundaries.
#To write: functions that
#         get data from file,
#         parse lines to location to stamp


import turtle

def setUpScreen():
     w = turtle.Screen()
     w.setworldcoordinates(-181,-91,181,91)
     return(w)

def drawOceans():
     infile = open("oceansSimplified.json","r")#A file with coordinates field only
     lines = infile.readlines()         #Read in the lines of the file

     for line in lines:                
          start = line.find("[[[")+1    #Find where the coordinates start
          end = line.find("]]]}")+2     #    and ends
          coordString = line[start:end] #Grab the coordinates, ignoring last 5 characters in line
                                        #    (not needed in our format)
          coordinates = eval(coordString)    #Turn the string into list of numbers
          print(coordinates[-1])
          turtle.up()                   #Move to starting point without drawing
          turtle.goto(coordinates[0][0], coordinates[0][1])
          turtle.down()
          #print coordinates
          for point in coordinates:     #For each point in the list of coordinates
               print(point)
               x = point[0]             #Find the x and y of point
               y = point[1]
               turtle.goto(x,y)         #Move the turtle to the (x,y)


def getQuakeData():
     #Open earthquake CSV file from USGS
     infile = open("week4.5_2015Mar18.csv","r")
     infile.readline()             #Ignore first line
     lines = infile.readlines()    #But store all the rest
     infile.close()
     return lines

def drawQuakes(lines):
     turtle.up()
     turtle.shape("turtle")
     turtle.shapesize(.5,.5)
     turtle.color("red")
     for line in lines:
          cells = line.split(",")
          time = cells[0]
          lat = float(cells[1])
          lon = float(cells[2])
          mag = float(cells[4])
          location = cells[13]
          print("There was an earthquake of magnitude",mag,"at (",lat,", ",lon,")",location)
          turtle.goto(lon,lat)
          turtle.stamp()

def main():
     w = setUpScreen()   #Set up the screen with lower left (-90,-180) and upper right (90,180)
     drawOceans()        #Draws oceans using the oceansSimplified.json file
     lines = getQuakeData()   #Asks user for quake file and returns list of lines
     drawQuakes(lines)   #Stamps at each point in each line
     w.exitonclick()     #Close the window when clicked

main()
