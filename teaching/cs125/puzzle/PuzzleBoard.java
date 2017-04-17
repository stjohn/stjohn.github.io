
// Demonstrating the Point and circles classes
// from ccj.

import ccj.*;

public class PuzzleBoard 
{
    PuzzlePiece[][] board;

    /** 
     * The default constructor-- sets up the board of puzzlePieces
     */

    public PuzzleBoard()
    {
	board = new PuzzlePiece[4][4];
	for (int i = 0; i < 4; i++)
	    for (int j = 0; j < 4; j++)
		board[i][j] = new PuzzlePiece( (i+j*4+1)%16,
				2+i*2, 2+j*2);
	board[3][3] = null; 	// Set bottom corner to empty
    }
  
    /**
     * Takes the point p and checks if it is within the "Scramble"
     * box.  If so, it calls the private method Scramble().
     * If not, it determines which square has been clicked (in terms
     * of the indices of the array) and calls a private method 
     * privateMethod with the indices.
     * @param p the location of the last mouse click
     */
    public void move(Point p)
    {

	if ( isScramble(p) )
	    Scramble();
	else 
	{
	    double x = p.getX();
	    double y = p.getY();
	    if ( (2 <= x) && (x <= 10) && (2 <= y) && (y <= 10) )
	    {
		int i = (int) Math.floor( x/2 - 1 ); 
		int j = (int) Math.floor( y/2 - 1 ); 
		privateMove(i,j);
	    }
	}
    }
  
    /**
     * Draws the board and the "Scramble" box.  
     * The puzzle pieces are drawn by calling the draw method
     * in PuzzlePiece.
     */
    public void draw()
    {
	new Line( new Point(4,0), new Point(8,0)).draw();
	new Line( new Point(4,1), new Point(8,1)).draw();
	new Line( new Point(4,0), new Point(4,1)).draw();
	new Line( new Point(8,0), new Point(8,1)).draw();
	new Message(new Point(4.5, .25), "Scramble").draw();
	for (int i = 0; i < 4; i++)
	    for (int j = 0; j < 4; j++)
		if ( board[i][j] != null )
		    board[i][j].draw();
    }

    /**
     * Given a point, checks if it's inside the "Scramble" box.
     * @param p the point the user clicked.
     * @return true if p is in the box, false otherwise.
     */
    private boolean isScramble(Point p)
    {
	double x = p.getX();
	double y = p.getY();

	if ( (4 <= x) && (x <= 8) && (0 <= y) && (y <= 1) )
	    return true;
	else 
	    return false;
    }

    /**
     * Scrambles the pieces by calling privateMove a 1000 times
     * with randomly generated indices.  
     * (This is called from move().).
     */

    private void Scramble()
    {
	for (int i = 0; i < 1000 ; i++)
	    privateMove( Numeric.randomInt(0,3), Numeric.randomInt(0,3));
    }

    /**
     * Takes the indices and checks for the place to move the piece.
     * This is where all the work takes place.  After finding the move,
     * the piece is moved to it's new position in the array, and it's
     * position on the board is updated using the move method in 
     * PuzzlePiece.
     * @param i the first index, ranges from 0 to 3
     * @param j the second index, ranges from 0 to 3
     */
    private void privateMove(int i, int j)
    {
	if ( board[i][j] != null ) 
	{
	    if ( i == 0 )
	    {
		if ( j == 0 )
		{
		    if ( board[1][0] == null )
		    {
			board[i][j].move(2,0);
			board[1][0] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[0][1] == null )
		    {
			board[i][j].move(0,2);
			board[0][1] = board[i][j];
			board[i][j] = null;
		    }
		}
		else if ( j == 3 )
		{
		    if ( board[0][2] == null )
		    {
			board[i][j].move(0,-2);
			board[0][2] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[1][3] == null )
		    {
			board[i][j].move(2,0);
			board[1][3] = board[i][j];
			board[i][j] = null;
		    }
		}
		else //  0 < j < 3
		{
		    if ( board[0][j-1] == null )
		    {
			board[i][j].move(0,-2);
		        board[0][j-1] = board[0][j];
			board[i][j] = null;
		    }
		    else if ( board[0][j+1] == null )
		    {
			board[i][j].move(0,2);
			board[0][j+1] = board[0][j];
			board[i][j] = null;
		    }
		    else if ( board[1][j] == null )
		    {
			board[i][j].move(2,0);
			board[1][j] = board[0][j];
			board[i][j] = null;
		    }
		}
	    }
	    else if ( i == 3 )	
	    { 
		if ( j == 0 )
		{
		    if ( board[2][0] == null )
		    {
			board[i][j].move(-2,0);
			board[2][0] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[3][1] == null )
		    {
			board[i][j].move(0,2);
			board[3][1] = board[i][j];
			board[i][j] = null;
		    }
		}
		else if ( j == 3 )
		{
		    if ( board[3][2] == null )
		    {
			board[i][j].move(0,-2);
			board[3][2] = board[i][i];
			board[i][j] = null;
		    }
		    else if ( board[2][3] == null )
		    {
			board[i][j].move(-2,0);
			board[2][3] = board[i][j];
			board[i][j] = null;
		    }
		}
		else //  0 < j < 3
		{
		    if ( board[3][j-1] == null )
		    {
			board[i][j].move(0,-2);
		        board[3][j-1] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[3][j+1] == null )
		    {
			board[i][j].move(0,2);
			board[3][j+1] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[2][j] == null )
		    {
			board[i][j].move(-2,0);
			board[2][j] = board[i][j];
			board[i][j] = null;
		    }
		}
	    }
	    else 	// 0 < i < 3
	    {
		if ( j == 0 )
		{
		    if ( board[i-1][0] == null )
		    {
			board[i][j].move(-2,0);
			board[i-1][0] = board[i][j];
			board[i][j] = null;
		    }
		    if ( board[i+1][0] == null )
		    {
			board[i][j].move(2,0);
			board[i+1][0] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[i][1] == null )
		    {
			board[i][j].move(0,2);
			board[i][1] = board[i][j];
			board[i][j] = null;
		    }
		}
		else if ( j == 3 )
		{
		    if ( board[i+1][3] == null )
		    {
			board[i][j].move(2,0);
			board[i+1][3] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[i-1][3] == null )
		    {
			board[i][j].move(-2,0);
			board[i-1][3] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[i][2] == null )
		    {
			board[i][j].move(0,-2);
			board[i][2] = board[i][j];
			board[i][j] = null;
		    }
		}
		else 	// 0 < i, j < 3
		{
		    if ( board[i][j-1] == null )
		    {
			board[i][j].move(0,-2);
		    	board[i][j-1] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[i-1][j] == null )
		    {
			board[i][j].move(-2,0);
		    	board[i-1][j] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[i+1][j] == null )
		    {
			board[i][j].move(2,0);
		    	board[i+1][j] = board[i][j];
			board[i][j] = null;
		    }
		    else if ( board[i][j+1] == null )
		    {
			board[i][j].move(0,2);
		    	board[i][j+1] = board[i][j];
			board[i][j] = null;
		    }
		}
	    }
	}
    }
}
