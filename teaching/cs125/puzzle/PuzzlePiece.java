
// Demonstrating the Point and circles classes
// from ccj.

import ccj.*;

public class PuzzlePiece 
{
    private Point ul;
    int label;


    /**
     * Initialize the label to 0 and the corner to (0,0).
     */

    public PuzzlePiece()
    {
	ul = new Point(0,0);
	label = 0;
    }
  

    /**
     * Initialize the label to l and the corner to (0,0).
     * @param l the label for the piece
     */

    public PuzzlePiece(int l)
    {
	ul = new Point(0,0);
	label = l;
    }
  

    /**
     * Initialize the label to l and the corner to (x,y).
     * @param l the label for the piece
     * @param x the x-coordinate of the corner.
     * @param y the y-coordinate of the corner.
     */

    public PuzzlePiece(int l, double x, double y)
    {
	ul = new Point(x,y);
	label = l;
    }


    /**
     * Move the piece by dx units in the x direction and dy units in the y 
     * direction.
     * @param dx change in x-coordinate
     * @param dy change in y-coordinate
     */

    public void move(int dx, int dy)
    {
	ul.move(dx,dy);
    }
  

    /**
     * Draw the puzzle piece.  The label is drawn, surrounded by
     * a square whose upper left corner is the point stored in
     * PuzzlePiece.
     */
    public void draw()
    {
	Point ll = new Point(ul.getX(), ul.getY()+2);
	Point lr = new Point(ul.getX()+2, ul.getY()+2);
	Point ur = new Point(ul.getX()+2, ul.getY());
	new Line( ul, ll).draw();
	new Line( ul, ur).draw();
	new Line( ll, lr).draw();
	new Line( ur, lr).draw();
	Message m = new Message(new Point(ul.getX()+.8, ul.getY()+.8), ""+label);
	m.draw();
    }
}
