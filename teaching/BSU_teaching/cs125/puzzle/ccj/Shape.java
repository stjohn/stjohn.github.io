/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Shape.java
** CHANGES:
****************************************************************************/

/**
 * The base class for shapes 
 * @version 1.00 28 Oct 1997
 * @author Cay Horstmann
 */

package ccj;

public abstract class Shape implements Cloneable
{  public void draw()
   {  GraphicsApplet.addShape(this);
   }

   abstract void redraw(java.awt.Graphics g, GraphicsCoord coord);
        
   public Object clone()
   {  try
      { return super.clone(); }
      catch(CloneNotSupportedException e)
      { return null; }
   }
}
