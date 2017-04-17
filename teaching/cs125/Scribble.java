// This example is modified from the book "Java in a Nutshell" 
// David Flanagan, O'Reilly & Associates, 1996.

import java.applet.*;   //Load in the applet class
import java.awt.*;      //Load in buttons and friends from the window class

public class Scribble extends Applet {
    private int last_x = 0;     //Keep track of x and y coordinate
    private int last_y = 0;     //When the mouse is clicked
    private Color current_color = Color.black;  //Current color of drawing pen
    
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
}
