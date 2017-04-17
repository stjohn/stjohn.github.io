/**
 * This program demonstrates an orbital program with 3 objects
 */

import java.applet.*;
import java.awt.*;
import java.math.*;
import java.net.*;
import java.util.*;

public class orbits2 extends Applet implements Runnable
{
    //Coordinates for first object:
    protected int[] xCoords1;	//Array that x coordinates
    protected int[] yCoords1;	//Array that y coordinates
    //Coordinates for second object:
    protected int[] xCoords2;	//Array that x coordinates
    protected int[] yCoords2;	//Array that y coordinates
    //Coordinates for third object:
    protected int[] xCoords3;	//Array that x coordinates
    protected int[] yCoords3;	//Array that y coordinates
    protected int current;		//The index of (x,y) being displayed
    private int numDisplayed = 1;  	//Number of points to display
    private int current_speed = 1000;	//Display speed
    private int t = -1;			//Time that has passed
    private int tail = 0;		//Tail that has been calculated
    private double period = 0;		//The period of the functions

    //Buttons displayed in the applet:
    private Button start_button;	//To start the animation
    private Button stop_button;		//To stop the animation
    private Choice num_choices;		//Choice for number of points displayed
    private Choice speed_choices; 	//Choice for display speed
    private TextField theText;		//To allow user to choose period
    private Button enter_button;	//To enter period
    private Panel text_panel;		//Panel for period
    private Panel button_panel;		//Panel for buttons and choices

    //
    //Here's the method that does all the work.  To change the
    //orbit displayed, change the function that calculates x1 and y1 (for
    //the first object), x2 and y2 (for the second), and x3 and y3 (for
    //the third)..
    //The functions that calculate x's and y's should have values 
    //between -1 and 1.
    //
    public void run()
    {
    	while (true)
	{
	    //Update counters:
	    current++;	t++;
	    if (current == xCoords1.length) current = 0;

	    //Calculate and store next set of points:
	    //Change the next two lines, if you'd like to calculate
	    //a different orbit.  Your functions should give a 
	    //value between -1 and 1.  t is a time parameter.
	    
	    double x1 = 0.5*Math.cos(t/50.0);
	    double y1 = 0.5*Math.sin(t/50.0);

	    double x2 = 0.75*Math.cos(t/50.0);
	    double y2 = 0.75*Math.sin(t/50.0);

	    double x3 = Math.cos(t/50.0);
	    double y3 = Math.sin(t/50.0);

	    //Scale (x,y) and store in an array of values
	    xCoords1[current] = (new Double(150*x1 + 200)).intValue();
	    yCoords1[current] = (new Double(150*y1 + 200)).intValue();
	    xCoords2[current] = (new Double(150*x2 + 200)).intValue();
	    yCoords2[current] = (new Double(150*y2 + 200)).intValue();
	    xCoords3[current] = (new Double(150*x3 + 200)).intValue();
	    yCoords3[current] = (new Double(150*y3 + 200)).intValue();

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
    	xCoords1 = new int[1000];	
    	yCoords1 = new int[1000];	
    	xCoords2 = new int[1000];	
    	yCoords2 = new int[1000];	
    	xCoords3 = new int[1000];	
    	yCoords3 = new int[1000];	

	//Set color and size:
        setSize(500, 400);
        setBackground(Color.blue);

        //Since there's so many buttons and things, use a layout manager
	//and panels to keep them from running altogether.
	setLayout(new BorderLayout());

	//The panel at the bottom for the user to enter period:
        text_panel = new Panel(); 
        text_panel.setBackground(Color.gray);

        // The label that tells the user what to enter:
        Label textLabel = new Label("Enter period:");
        text_panel.add(textLabel);

        // The text field for entering the number:
        theText = new TextField(6);
        theText.setBackground(Color.lightGray);
        text_panel.add(theText);

        // The enter button (pushed after you enter the new period):
        enter_button = new Button("Enter");
        text_panel.add(enter_button);
        enter_button.setForeground(Color.black);
        enter_button.setBackground(Color.lightGray);
        add(text_panel, "South");

	//The panel at the top for the buttons and choices
        button_panel = new Panel(); 
        button_panel.setBackground(Color.gray);

        // Create a button and add it to the graphics window
        stop_button = new Button("stop");//Make the label also say "stop"
        stop_button.setForeground(Color.black);
        stop_button.setBackground(Color.lightGray);
        button_panel.add(stop_button);            //Necessary to use the button

        // Create a button and add it to the graphics window
        start_button = new Button("start");//Make the label also say "start"
        start_button.setForeground(Color.black);
        start_button.setBackground(Color.lightGray);
        button_panel.add(start_button);            //Necessary to use the button

        // Create choices with items for the colors and add it to
        // the graphics window
        num_choices = new Choice();
        num_choices.addItem("1");
        num_choices.addItem("10");
        num_choices.addItem("100");
        num_choices.setForeground(Color.black);
        num_choices.setBackground(Color.lightGray);
        button_panel.add(new Label("Tail:"));
        button_panel.add(num_choices);

        // Create choices with items for the display speed and add it to
        // the graphics window
        speed_choices = new Choice();
        speed_choices.addItem("slow");
        speed_choices.addItem("medium");
        speed_choices.addItem("fast");
        speed_choices.setForeground(Color.black);
        speed_choices.setBackground(Color.lightGray);
        button_panel.add(new Label("Speed:"));
        button_panel.add(speed_choices);

	//Add the button panel to the top:
        add(button_panel, "North");
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

		g.setColor(Color.orange);
        	g.fillRect(xCoords1[j], yCoords1[j],2,2);
		g.setColor(Color.pink);
        	g.fillRect(xCoords2[j], yCoords2[j],2,2);
		g.setColor(Color.red);
        	g.fillRect(xCoords3[j], yCoords3[j],2,2);
	    }
	    else
	    {
		g.setColor(Color.orange);
        	g.fillRect(xCoords1[current-i], yCoords1[current-i],2,2);
		g.setColor(Color.pink);
        	g.fillRect(xCoords2[current-i], yCoords2[current-i],2,2);
		g.setColor(Color.red);
        	g.fillRect(xCoords3[current-i], yCoords3[current-i],2,2);
	    }
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
        else if (event.target == stop_button) {
	    this.stop();
            return true;
        }
        else if (event.target == enter_button) {
	    period = Double.valueOf(theText.getText().trim()).doubleValue();
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


