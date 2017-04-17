
// Demonstrating the Point and circles classes
// from ccj.

import ccj.*;

public class Manager extends GraphicsApplet
{
    public void run()
    {
      	PuzzleBoard game = new PuzzleBoard();
	setCoord(0,0,12,12);
     
      	while ( true )
      	{
	    clearWindow();
	    game.draw();
 	    Point p = readMouse("Click on piece to move or 'Scramble':");
	    game.move(p);
	    game.draw();
	}
    }
}
