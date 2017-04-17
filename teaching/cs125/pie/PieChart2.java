/* For Group Work, CS 125, Spring 1999
 * 
 *  P3.15: Ask user for 4 inputs and draw pie chart
 *
 *  Second stage: declare variables and do the easy steps of getting the
 *                input and drawing outer circle.
 *                Add an extra line to make sure the numbers are being 
 *                read in correctly (to be removed later).
 *                Compile and make sure it works before going on.
 */
 
import ccj.*;
 
public class PieChart2 extends GraphicsApplet
{
  public void run()
  {
    // Ask user for 4 inputs:
    int num1 = readInt("Please enter first number:");
    int num2 = readInt("Please enter second number:");
    int num3 = readInt("Please enter third number:");
    int num4 = readInt("Please enter fourth number:");
    
    // Testing line:
    String test = "The numbers are " + num1 + ", " + num2
                + ", " + num3 + ", " + num4;
    new Message(new Point(-9,-9), test).draw();
    
    // Draw outer circle of pie chart
    Point center = new Point(0,0);	// Make an object for center since 
                                    // we'll over and over again
    Circle c = new Circle(center, 5);
    c.draw();
    
    // Draw initial line (along positive x-axis)
    new Line(center, new Point(5,0)).draw(); // Can also break this up 
                                    // into several steps
                                
    // Calculate first angle and draw second line
    // Calculate second angle and draw third line
    // Calculate third angle and draw fourth line
  }
}
