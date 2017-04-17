/**
 * This program demonstrates an orbital program 
 */

import java.applet.*;
import java.awt.*;
import java.math.*;
import java.net.*;
import java.util.*;

public class orbits extends Applet implements Runnable
{
    protected int[] xCoords;	//Array that x coordinates
    protected int[] yCoords;	//Array that y coordinates
    protected int current;		//The index of (x,y) being displayed
    private int numDisplayed = 1;  	//Number of points to display
    private int current_speed = 1000;	//Display speed
    private int t = -1;			//Time that has passed
    private int tail = 0;		//Tail that has been calculated

    //Buttons displayed in the applet:
    private Button start_button;	//To start the animation
    private Button stop_button;		//To stop the animation
    private Choice num_choices;		//Choice for number of points displayed
    private Choice speed_choices; 	//Choice for display speed

    //
    //Here's the method that does all the work.  To change the
    //orbit displayed, change the function that calculates x and y.
    //The functions that calculate x and y should have values 
    //between -1 and 1.
    //
    public void run()
    {
    	while (true)
	{
	    //Update counters:
	    current++;	t++;
	    if (current == xCoords.length) current = 0;

	    //Calculate and store next set of points:
	    //Change the next two lines, if you'd like to calculate
	    //a different orbit.  Your functions should give a 
	    //value between -1 and 1.  t is a time parameter.
	    
	    double x = Math.cos(t/50.0);
	    double y = Math.sin(t/50.0);

	    //Scale (x,y) and store in an array of values
	    xCoords[current] = (new Double(150*x + 200)).intValue();
	    yCoords[current] = (new Double(150*y + 200)).intValue();

	    //Size of tail that has been already calculated:
	    if ( tail < numDisplayed )
		tail++;

	    //Refresh the image:
	    this.repaint();

	    //Sleep to keep image from being displayed too quickly:
	    try {
	    	Thread.sleep(current_speed);
	    }
	    catch (InterruptedException e) { ; }
	}
    }

    //Set up everything up (buttons, etc). 
    public void init()
    {
	//Set up arrays:
    	xCoords = new int[1000];	
    	yCoords = new int[1000];	

	//Set color and size:
        setSize(500, 400);
        setBackground(Color.blue);

        // Create a button and add it to the graphics window
        stop_button = new Button("stop");//Make the label also say "stop"
        stop_button.setForeground(Color.black);
        stop_button.setBackground(Color.lightGray);
        this.add(stop_button);            //Necessary to use the button

        // Create a button and add it to the graphics window
        start_button = new Button("start");//Make the label also say "start"
        start_button.setForeground(Color.black);
        start_button.setBackground(Color.lightGray);
        this.add(start_button);            //Necessary to use the button

        // Create choices with items for the colors and add it to
        // the graphics window
        num_choices = new Choice();
        num_choices.addItem("1");
        num_choices.addItem("10");
        num_choices.addItem("100");
        num_choices.setForeground(Color.black);
        num_choices.setBackground(Color.lightGray);
        this.add(new Label("Tail:"));
        this.add(num_choices);

        // Create choices with items for the display speed and add it to
        // the graphics window
        speed_choices = new Choice();
        speed_choices.addItem("slow");
        speed_choices.addItem("medium");
        speed_choices.addItem("fast");
        speed_choices.setForeground(Color.black);
        speed_choices.setBackground(Color.lightGray);
        this.add(new Label("Speed:"));
        this.add(speed_choices);
    }

    //This is the thread that runs the animation and the 
    //methods that start and stop it:
    private Thread animate_thread = null;

    public void start()
    {
    	if (animate_thread == null)
	{
	    animate_thread = new Thread(this);
	    animate_thread.start();
	}
    }

    public void stop()
    {
    	if ((animate_thread != null) && animate_thread.isAlive())
	{
	    animate_thread.stop();
	}

	//Set to null, so, it can be picked up by garbage collection
	animate_thread = null;
    }


    //Paints the orbit to the screen
    public void paint(Graphics g)
    {
	g.setColor(Color.green);
	for (int i = 0; i < tail; i++)
	{
	    if ( current - i < 0 )
	    {
		int j = 1000 + (current-i);
        	g.fillRect(xCoords[j], yCoords[j],2,2);
	    }
	    else
        	g.fillRect(xCoords[current-i],
			yCoords[current-i],2,2);
	}
    }

    //Handles the buttons and choices:
    public boolean action(Event event, Object arg) 
    {
        // If the Clear button was clicked, clear the graphics window
        if (event.target == start_button) {
	    this.start();
            return true;
        }
        if (event.target == stop_button) {
	    this.stop();
            return true;
        }
        else if (event.target == num_choices) {
            if (arg.equals("1"))
	    {
		numDisplayed = 1;
		if ( tail > numDisplayed )
		    tail = numDisplayed;
	    }
            else if (arg.equals("10")) 
	    {
		numDisplayed = 10;
		if ( tail > numDisplayed )
		    tail = numDisplayed;
	    }
            else if (arg.equals("100")) 
	    {
		numDisplayed = 100;
		if ( tail > numDisplayed )
		    tail = numDisplayed;
	    }
            return true;
        }
        else if (event.target == speed_choices) {
            if (arg.equals("slow")) current_speed = 500;
            else if (arg.equals("medium")) current_speed = 250;
            else if (arg.equals("fast")) current_speed = 100;
            return true;
        }
        // Otherwise, let the superclass handle it.
        else return super.action(event, arg);
    }
}


