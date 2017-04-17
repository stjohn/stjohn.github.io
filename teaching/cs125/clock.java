
// This program makes an analog clock face that
// displays the current time.
//
// It uses the GraphicsApplet from ccj.*

import ccj.*;

public class clock extends GraphicsApplet
{
    public void run()
    {
	// The outer circle of the clock:
	Point center = new Point(0,0);
	Circle c = new Circle(center, 5);

	// Get the current time
	Time now = new Time();
	int minutes = now.getMinutes();
	int hours = now.getHours();

	// Calculate the angle of hands (in radians):
	double angleMin = minutes * ( 360.0 / 60 ) 
		* ( Math.PI / 180 );
	double angleHour = (hours*60 + minutes) 
		* ( 360.0 / (12*60) )
		* ( Math.PI / 180.0 );

	// Calculate the coordinates of the hands:
	Point minPt = new Point( 4* Math.sin(angleMin),
		4 * Math.cos(angleMin));
	Point hourPt = new Point( 2.5* Math.sin(angleHour),
		2.5 * Math.cos(angleHour));

	// Make and draw hands:
	Line minHand = new Line(center, minPt);
	Line hourHand = new Line(center, hourPt);

	// Draw the clock:
	c.draw();
	minHand.draw();
	hourHand.draw();	

	// Display message:
	String minSt = "0" + minutes;
	int length = minSt.length();
	String timeis = "The time is " + hours + ":" 
		+ minSt.substring(length-2,length) + ".";
	Message time = new Message(new Point(-8,-8), timeis);
	time.draw();
    }
}
