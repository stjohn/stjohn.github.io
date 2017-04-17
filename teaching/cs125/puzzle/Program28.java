/*
 * This class sets up a PuzzleBoard and repeatedly draws 
 * the board, gets the next move, and passes the move to 
 * the PuzzleBoard to handle.
 *
 * Uses GraphicsApplet from ccj.
 * 
 */

import ccj.*;

public class Program25 extends GraphicsApplet
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
	}
    }
}
