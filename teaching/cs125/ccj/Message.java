/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Message.java
** CHANGES:
   28 Oct 1997       Cloned Point objects in constructor and accessors
****************************************************************************/

/**
 * A messge for labeling simple graphics
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;

public class Message extends Shape
{  /**
    * Creates a new message object
    * @param p the top left corner of the message
    * @param s the text of the message
    */

   public Message(Point p, String s)
   {  start = (Point)p.clone();
      text = s;
   }

   /**
    * Default constructor
    */

   public Message() /* CSH 1998-02-28 */
   {  start = new Point();
      text = "";
   }

   /**
    * Moves this graphical shape
    * @param dx the amount to move by in x direction
    * @param dy the amount to move by in y direction
    */

   public void move(double x, double y)
   {  start.move(x, y);
   }

   /**
    * Creates a copy of this object
    * @return a copy of this object
    */

   public Object clone()
   {  Message r = (Message)super.clone();
      r.start = (Point)start.clone();
      return r;
   }

   void redraw(java.awt.Graphics g, GraphicsCoord coord)
   {  int y = coord.yToPixelPos(start.getY());
      y += g.getFontMetrics().getAscent();
         g.drawString(text, coord.xToPixelPos(start.getX()), y);
   }
            
   /**
    * Creates a string representation of this object
    * @return a string representation of this object
    */

   public String toString()
   {  return "Message[start = " + start.toString() + "," + "text = " + text + "]";
   }

   /**
    * Tests if this object equals another
    * @param b the object to compare with
    * @return <tt>true</tt> if the two objects are equal
    */

   public boolean equals(Object b)
   {  if (b instanceof Message)
      {  Message pb = (Message)b;
         return start.equals(pb.start) && text.equals(pb.text);
      }
      else return false;
   }

   /**
    * Computes a hash code for this object
    * @return a hash code for this object
    */

   public int hashCode()
   {  return 29 * start.hashCode() + 31 * text.hashCode();
   }

   /**
    * Gets the top left corner of the message 
    * @return the top left corner of the message 
    */

   public Point getStart()
   {  return (Point)start.clone();
   }

   /**
    * Gets the text of the message 
    * @return the text of the message 
    */

   public String getText()
   {  return text;
   }

   private Point start;
   private String text;
}




