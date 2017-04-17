/* For Group Work, CS 125, Spring 1999
 * 
 *  P3.15: Ask user for 4 inputs and draw pie chart
 *
 *  Third stage: Calculate first angle.  Run test cases to make sure
 *                calculation is correct.
 *                Remove the line added to test if numbers were being
 *                read in.
 *                Compile and make sure it works before going on.
 */
 
import ccj.*;
 
public class PieChart3 extends GraphicsApplet
{
  public void run()
  {
    // Ask user for 4 inputs:
    int num1 = readInt("Please enter first number:");
    int num2 = readInt("Please enter second number:");
    int num3 = readInt("Please enter third number:");
    int num4 = readInt("Please enter fourth number:");
    
    // Draw outer circle of pie chart
    Point center = new Point(0,0);	// Make an object for center since 
                                    // we'll over and over again
    Circle c = new Circle(center, 5);
    c.draw();
    
    // Draw initial line (along positive x-axis)
    new Line(center, new Point(5,0)).draw(); // Can also break this up 
                                    // into several steps
                                
    // Calculate first angle and draw second line
    double total = num1 + num2 + num3 + num4; // total size of pie
    double theta1 = (num1/total)*2*Math.PI; // fraction of pie for num1
    double x1 = 5 * Math.cos(theta1); // 5 is the radius of the circle
    double y1 = 5 * Math.sin(theta1);  
    
    new Line(center, new Point(x1,y1)).draw();
    
    // Calculate second angle and draw third line
    // Calculate third angle and draw fourth line
  }
}
