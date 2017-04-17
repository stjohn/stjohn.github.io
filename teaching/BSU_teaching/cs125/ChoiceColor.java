// This example is modified from the book "Java in a Nutshell" 
// David Flanagan, O'Reilly & Associates, 1996.

import java.applet.*;	//Load in the applet class
import java.awt.*;	//Load in buttons and friends from the window class

public class ChoiceColor extends Applet {
    private int last_x = 0;	//Keep track of x and y coordinate
    private int last_y = 0;	//When the mouse is clicked
    private Button clear_button;
    private Color current_color = Color.black;  //Current color of drawing pen
    private Choice color_choices;
    
    // This function is called initially, when the program begins
    // executing.  It initializes the graphics window.
    
    public void init() {
        this.setBackground(Color.white);   //Set the background color
  
        // Create a button and add it to the graphics window
        clear_button = new Button("Clear");//Make the label also say "Clear"
        clear_button.setForeground(Color.black);
        clear_button.setBackground(Color.lightGray);
        this.add(clear_button);            //Necessary to use the button

	// Create choices with items for the colors and add it to
	// the graphics window
	color_choices = new Choice();
	color_choices.addItem("black");
	color_choices.addItem("red");
	color_choices.addItem("blue");
	color_choices.addItem("green");
        color_choices.setForeground(Color.black);
        color_choices.setBackground(Color.lightGray);
	//this.add(new Label("Color: "));
	this.add(color_choices);
    }

    
    // Called when the user clicks the mouse to start a scribble
    // Sets the values of variables last_x and last_y to mark the
    // point of the click.

    public boolean mouseDown(Event e, int x, int y)
    {
        last_x = x; last_y = y;		//Store the coordinates when 
        return true;		//and don't do anything else (that is, the
        			//"event handled" is true)
    }

    
    // Called when the user draws with the mouse button down
    // Draws a line between the points (last_x, last_y) and (x, y)
    
    public boolean mouseDrag(Event event, int x, int y)
    {
        Graphics g = this.getGraphics(); //Necessary to draw to the screen
        g.setColor(current_color);	 //Line will be current_color
        g.drawLine(last_x, last_y, x, y);//Draws the line
        last_x = x;	//Saves (x,y) in last (last_x, last_y), so that
        last_y = y;	//the next line drawn will start from these points
        return true;	//and don't do anything else ("event handled").
    }


    // Called when the user clicks the Clear button, and 
    // clears the graphics window, or when the user chooses
    // a different color using the Choice button.
    
    public boolean action(Event event, Object arg) 
    {
        // If the Clear button was clicked, clear the graphics window
        if (event.target == clear_button) {
            Graphics g = this.getGraphics();
            Rectangle r = this.bounds();
            g.setColor(this.getBackground());
            g.fillRect(r.x, r.y, r.width, r.height);
            return true;
        }
	else if (event.target == color_choices) {
	    if (arg.equals("black")) current_color = Color.black;
	    else if (arg.equals("red")) current_color = Color.red;
	    else if (arg.equals("blue")) current_color = Color.blue;
	    else if (arg.equals("green")) current_color = Color.green;
	    return true;
	}
        // Otherwise, let the superclass handle it.
        else return super.action(event, arg);
    }

}
