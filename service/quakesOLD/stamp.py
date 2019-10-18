#These Python commands create a turtle (named tracy) and stamp at (0,0) and (100,50)	
#Use the turtle library:
import turtle	
#Create a turtle, tracy, that's green and turtle-shaped.
tracy = turtle.Turtle()
tracy.shape('turtle')
tracy.color('green')


#Lift the pen up, so, that only the stamps show on the screen (not also the path)
tracy.penup()

#Stamp at the starting location, (0,0)
tracy.stamp()

#Move to (100,50) and stamp:	
tracy.goto(100,50)
tracy.stamp()

#How big is the default screen?  
#What the largest (and smallest) coordinates that tracy can stamp and show on the screen?
