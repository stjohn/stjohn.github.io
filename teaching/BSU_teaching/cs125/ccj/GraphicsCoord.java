/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             GraphicsCoord.java
** CHANGES:
****************************************************************************/

/**
 * Pixel independent graphics coordinates 
 * @version 1.00 28 Oct 1997
 * @author Cay Horstmann
 */

package ccj;

class GraphicsCoord
{  static final int INSETS = 3;

   void setCoord(double x1, double y1, double x2, double y2)
   {  xleft = x1;
      ytop = y1;
      xright = x2;
      ybottom = y2;
   }

   void setPixel(int w, int h)
   {  xwidth = w;
      yheight = h;
   }

   public int xToPixelPos(double x)
   {  return INSETS + (int)Math.round((xwidth - 2 * INSETS)
         * (x - xleft) / (xright - xleft));
   }

   public int yToPixelPos(double y)
   {  return INSETS + (int)Math.round((yheight - 2 * INSETS)
         * (y - ytop) / (ybottom - ytop));
   }

   public int xToPixelDist(double x)
   {  return (int)Math.round((xwidth - 2 * INSETS)
         * x / (xright - xleft));
   }

   public int yToPixelDist(double y)
   {  return (int)Math.round((yheight - 2 * INSETS)
         * y / (ybottom - ytop));
   }

   public double xFromPixelPos(int x)
   {  return xleft + (xright - xleft)
         * (x - INSETS) / (xwidth - 2 * INSETS);
   }

   public double yFromPixelPos(int y)
   {  return ytop + (ybottom - ytop)
         * (y - INSETS) / (yheight - 2 * INSETS);
   }


   private int xwidth;
   private int yheight;
   private double xleft;
   private double xright;
   private double ytop;
   private double ybottom;
}
