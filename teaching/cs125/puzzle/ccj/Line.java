/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Line.java
** CHANGES:
   28 Oct 1997       Cloned Point objects in constructor and accessors
****************************************************************************/

/**
 * A line shape for simple graphics
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;

public class Line extends Shape
{  /**
    * Constructs a line object
    * @param s the starting point of the line
    * @param e the ending point of the line
    */

   public Line(Point s, Point e)
   {  start = (Point)s.clone();
      end = (Point)e.clone();
   }

   /**
    * Default constructor
    */

   public Line() /* CSH 1998-02-28 */
   {  start = new Point();
      end = new Point();
   }

   /**
    * Moves this graphical shape
    * @param dx the amount to move by in x direction
    * @param dy the amount to move by in y direction
    */

   public void move(double x, double y)
   {  start.move(x, y);
      end.move(x, y);
   }

   /**
    * Creates a copy of this object
    * @return a copy of this object
    */

   public Object clone()
   {  Line r = (Line)super.clone();
      r.start = (Point)start.clone();
      r.end = (Point)end.clone();
      return r;
   }

   void redraw(java.awt.Graphics g, GraphicsCoord coord)
   {  g.drawLine(coord.xToPixelPos(start.getX()), coord.yToPixelPos(start.getY()), 
         coord.xToPixelPos(end.getX()), coord.yToPixelPos(end.getY()));
   }
    
   /**
    * Creates a string representation of this object
    * @return a string representation of this object
    */

   public String toString()
   {  return "Line[start = " + start.toString() + "," + "end = " + end.toString() + "]";
   }

   /**
    * Tests if this object equals another
    * @param b the object to compare with
    * @return <tt>true</tt> if the two objects are equal
    */

   public boolean equals(Object b)
   {  if (b instanceof Line)
      {   Line pb = (Line)b;
          return start.equals(pb.start) && end.equals(pb.end);
      }
      else return false;
   }

   /**
    * Computes a has code for this object
    * @return a hash code for this object
    */

   public int hashCode()
   {  return 13 * start.hashCode() + 17 * end.hashCode();
   }

   /**
    * Gets the starting point of the line
    * @return the starting point of the line
    */

   public Point getStart()
   {  return (Point)start.clone();
   }

   /**
    * Gets the ending point of the line
    * @return the ending point of the line
    */

   public Point getEnd()
   {  return (Point)end.clone();
   }

   private Point start;
   private Point end;
}


