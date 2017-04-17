// This example is modified from the book "Java in a Nutshell" 
// David Flanagan, O'Reilly & Associates, 1996.

import java.applet.*;   //Load in the applet class
import java.awt.*;      //Load in buttons and friends from the window class

public class ThreeColorDraw extends Applet {
    private int last_x = 0;     //Keep track of x and y coordinate
    private int last_y = 0;     //When the mouse is clicked
    private Color current_color = Color.black;  //Current color of drawing pen
    private Button clear_button;        //Declare space for the clear button
    private Button red_button;        //Declare space for the red button
    private Button blue_button;        //Declare space for the blue button
    private Button black_button;        //Declare space for the black button
    
    // This function is called initially, when the program begins
    // executing.  It initializes the graphics window.
    
    public void init() {
        //this.setBackground(Color.white);   //Set the background color
  
        // Create a button and add it to the graphics window
        clear_button = new Button("Clear");//Make the label also say "Clear"
        clear_button.setForeground(Color.black);
        clear_button.setBackground(Color.lightGray);
        this.add(clear_button);            //Necessary to use the button

        red_button = new Button("Red");//Make the label also say "Red"
        red_button.setForeground(Color.red);
        red_button.setBackground(Color.lightGray);
        this.add(red_button);            //Necessary to use the button
	
        blue_button = new Button("Blue");//Make the label also say "Blue"
        blue_button.setForeground(Color.blue);
        blue_button.setBackground(Color.lightGray);
        this.add(blue_button);            //Necessary to use the button

        black_button = new Button("Black");//Make the label also say "Clear"
        black_button.setForeground(Color.black);
        black_button.setBackground(Color.lightGray);
        this.add(black_button);            //Necessary to use the button
        
    }
    
    // Called when the user clicks the mouse to start a scribble
    // Sets the values of variables last_x and last_y to mark the
    // point of the click.
    
    public boolean mouseDown(Event e, int x, int y)
    {
        last_x = x; last_y = y; //Store the coordinates when the mouse clicked
        return true;            //and don't do anything else (that is, the
                                //"event handled" is true)
    }
    
    // Called when the user draws with the mouse button down
    // Draws a line between the points (last_x, last_y) and (x, y)
    
    public boolean mouseDrag(Event event, int x, int y)
    {
        Graphics g = this.getGraphics(); //Necessary to draw to the screen
        g.setColor(current_color);       //Line will be current_color
        g.drawLine(last_x, last_y, x, y);//Draws the line
        last_x = x;     //Saves (x,y) in last (last_x, last_y), so that
        last_y = y;     //the next line drawn will start from these points
        return true;    //and don't do anything else ("event handled").
    }

    // Called when the user clicks the Clear button, and 
    // clears the graphics window.
    
    public boolean action(Event event, Object arg) {
        // If the Clear button was clicked, clear the graphics window
        if (event.target == clear_button) {
            Graphics g = this.getGraphics();
            Rectangle r = this.bounds();
            g.setColor(this.getBackground());
            g.fillRect(r.x, r.y, r.width, r.height);
            return true;
        }
        else if (event.target == red_button) {
	    current_color = Color.red;
            return true;
        }
        else if (event.target == blue_button) {
	    current_color = Color.blue;
            return true;
        }
        else if (event.target == black_button) {
	    current_color = Color.black;
            return true;
        }
        // Otherwise, let the superclass handle it.
        else return super.action(event, arg);
    }
}
