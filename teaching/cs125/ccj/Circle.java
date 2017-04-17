/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Circle.java
** CHANGES:
   28 Oct 1997       Cloned Point objects in constructor and accessors
****************************************************************************/

/**
 * A circle shape for simple graphics
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;

public class Circle extends Shape
{  /**
    * Constructs a circle
    * @param c the center of the circle
    * @param r the radius of the circle
    */

   public Circle(Point c, double r)
   {  center = (Point)c.clone();
      radius = r;
   }

   /**
    * Default constructor
    */

   public Circle() /* CSH 1998-02-28 */
   {  center = new Point();
      radius = 0;
   }

   /**
    * Moves this graphical shape
    * @param dx the amount to move by in x direction
    * @param dy the amount to move by in y direction
    */

   public void move(double x, double y)
   {  center.move(x, y);
   }

   /**
    * Gets the center of the circle
    * @return the center of the circle
    */

   public Point getCenter()
   {  return (Point)center.clone();
   }

   /**
    * Gets the radius of the circle
    * @return the radius of the circle
    */

   public double getRadius()
   {  return radius;
   }

   /**
    * Creates a copy of this object
    * @return a copy of this object
    */

   public Object clone()
   {  Circle r = (Circle)super.clone();
      r.center = (Point)center.clone();
      return r;
   }

   void redraw(java.awt.Graphics g, GraphicsCoord coord)
   {  int xrad = Math.abs(coord.xToPixelDist(radius));
      int yrad = Math.abs(coord.yToPixelDist(radius));
      int xtop = coord.xToPixelPos(center.getX()) - xrad;
      int ytop = coord.yToPixelPos(center.getY()) - yrad;
      g.drawOval(xtop, ytop, 2 * xrad, 2 * yrad);
   }

   /**
    * Creates a string representation of this object
    * @return a string representation of this object
    */

   public String toString()
   {  return "Circle[center = " + center.toString() + "," + "radius = " + radius + "]" ;
   }

   /**
    * Tests if this object equals another
    * @param b the object to compare with
    * @return <tt>true</tt> if the two objects are equal
    */

   public boolean equals(Object b)
   {  if (b instanceof Circle)
      {  Circle pb = (Circle)b;
         return center.equals(pb.center) && radius == pb.radius;
      }
      else return false;
   }
    
   /**
    * Computes a hash code for this object
    * @return a hash code for this object
    */

   public int hashCode()
   {  return (int)(19 * center.hashCode() + 23 * radius);
   }

   private Point center;
   private double radius;
}


