
// Demonstrating the Point and circles classes
// from ccj.

import ccj.*;

public class RandomWalk extends GraphicsApplet
{
    public void run()
    {
      String answer;

      do{
        // Clear window:
        clearWindow();

        // Draw grid:
        for (int i = -10 ; i <= 10 ; i = i+1)
        {
            Line vert = new Line(new Point(i,-10),
                                new Point(i,10));
            vert.draw();
            Line hor = new Line(new Point(-10,i),
                                new Point(10,i));
            hor.draw();
        }

        Point p = new Point(0,0);
        new Circle(p, .25).draw();

        p.draw();
        int i;

        for (i = 0 ; i < 100; i++)
        {
            int direction = Numeric.randomInt(1,4);
            if ( direction == 1 )
            {
                // Go north
                p.move(0,1);
                p.draw();
            } 
            else if ( direction == 2 )
            {
                // Go east
                p.move(1,0);
                p.draw();
            } 
            else if ( direction == 3 )
            {
                // Go south
                p.move(0,-1);
                p.draw();
            } 
            else // direction == 4
            {
                // Go west
                p.move(-1,0);
                p.draw();
            } 
        }
        new Circle(p, .25).draw();
        
        answer = readString("Would you like to try again?");
        answer = answer.substring(0,1);
      } while ( answer.equals("y") || answer.equals("Y"));

      answer = readString("Thank you for playing!");
    }
}

