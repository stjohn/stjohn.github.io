/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             GraphicsApplet.java
** CHANGES:
   28 Oct 1997       Split off Shape.java, GraphicsCoord.java
                     Fixed clearWindow
                     Moved coord to GraphCanvas, fixed mouse tracking bug
                     Added a blank label at the bottom because the 1.1 applet
                     viewer overwrites the bottom of the applet with status
                     line chatter
****************************************************************************/

/**
 * An applet for drawing simple graphics and getting user input
 * @version 1.01 28 Oct 1997
 * @author Cay Horstmann
 */

package ccj;

public abstract class GraphicsApplet extends java.applet.Applet implements Runnable
{  /**
    * Constructs a graphics applet
    */

   public GraphicsApplet()
   {  theApplet = this;
   }

   public void start()
   {  if (runner == null)
      {  runner = new Thread(this);
         runner.start();
      }
      else if (runner.isAlive())
         runner.resume();
   }

   public void stop()
   {  if (runner != null && runner.isAlive())
         runner.suspend();
   }

   /**
    * Define this method in your graphics applet class to draw graphics and get user input
    */

   public abstract void run();

   private void add(java.awt.Component c, java.awt.GridBagLayout gbl,
         java.awt.GridBagConstraints gbc, int x, int y, int w, int h)
   {  gbc.gridx = x;
      gbc.gridy = y;
      gbc.gridwidth = w;
      gbc.gridheight = h;
      gbl.setConstraints(c, gbc);
      add(c);
   }

   public void init()
   {  java.awt.GridBagLayout gbl = new java.awt.GridBagLayout();
      setLayout(gbl);
      java.awt.GridBagConstraints gbc = new java.awt.GridBagConstraints();
      gbc.weightx = 100;
      gbc.weighty = 100;
      gbc.fill = java.awt.GridBagConstraints.BOTH;
      graph = new GraphicsCanvas();
      add(graph, gbl, gbc, 0, 0, 2, 1);
      gbc.weighty = 0;
      gbc.fill = java.awt.GridBagConstraints.HORIZONTAL;
      label = new java.awt.Label();
      add(label, gbl, gbc, 0, 1, 2, 1);
      textbox = new java.awt.TextField();
      add(textbox, gbl, gbc, 0, 2, 1, 1);
      gbc.weightx = 0;
      java.awt.Button enter = new java.awt.Button("Enter");
      add(enter, gbl, gbc, 1, 2, 1, 1);
      add(new java.awt.Label(), gbl, gbc, 0, 3, 1, 1);
      graph.setCoord(-10, 10, 10, -10);
   }

   /**
    * Prompts user for mouse input
    * @param s the prompt string
    * @return the position at which the user clicked the mouse in response
    */

   public synchronized Point readMouse(String s)
   {  tracking = s;
      label.setText(s);
      while (clicked == null)
      {  try { wait(); } catch(InterruptedException e) {}
      }
      Point r = clicked;
      clicked = null;
      label.setText("");
      return r;
   }

   public boolean mouseMove(java.awt.Event evt, int x, int y)
   {  if (tracking != null)
      {  java.awt.Rectangle bounds = graph.bounds();
         if (bounds.inside(x, y))
         {  x -= bounds.x;
            y -= bounds.y;
            Point p = graph.getPointFromPixelPosition(x, y);
            label.setText(tracking + " (" + p.getX() + ","
               + p.getY() + ")");
            return true;
         }
         else
            label.setText(tracking);
      }
      return true;
   }

   public synchronized boolean mouseDown(java.awt.Event evt, int x, int y)
   {  if (tracking != null)
      {  java.awt.Rectangle bounds = graph.bounds();
         if (bounds.inside(x, y))
         {  x -= graph.bounds().x;
            y -= graph.bounds().y;
            clicked = graph.getPointFromPixelPosition(x, y);
            label.setText(tracking + " (" + clicked.getX() + ","
               + clicked.getY() + ")");
            tracking = null;
            notify();
            return true;
         }
      }
      return false;
   }

   public synchronized boolean action(java.awt.Event evt, Object arg)
   {  if (arg.equals("Enter"))
      {  text = textbox.getText();
         textbox.setText("");
         notify();
         return true;
      }
      return false;
   }

   public synchronized boolean keyDown(java.awt.Event evt, int key)
   {  if (key == '\n')
      {  text = textbox.getText();
         textbox.setText("");
         notify();
         return true;
      }
      return false;
   }

   private synchronized String readInput(String s)
   {  label.setText(s);
      textbox.requestFocus();
      while (text == null)
      {  try { wait(); } catch(InterruptedException e) {}
      }
      String r = text;
      text = null;
      label.setText("");

      return r;
   }

   /**
    * Prompts user for a string input
    * @param s the prompt string
    * @return the string the user typed in response
    */

   public static String readString(String s)
   {  return theApplet.readInput(s);
   }

   /**
    * Prompts user for an integer input
    * @param s the prompt string
    * @return the integer the user typed in response
    */

   public static int readInt(String s)
   {  try
      {  return Integer.valueOf(readString(s).trim()).intValue();
      }
      catch(NumberFormatException e)
      {  return 0;
      }
   }

   /**
    * Prompts user for a floating point input
    * @param s the prompt string
    * @return the floating point number the user typed in response
    */

   public static double readDouble(String s)
   {  try
      {  return Double.valueOf(readString(s).trim()).doubleValue();
      }
      catch(NumberFormatException e)
      {  return 0;
      }
   }

   /**
    * Clears the drawing window 
    */

   public static void clearWindow()
   {  theApplet.graph.shapes = new java.util.Vector();
      java.awt.Dimension d = theApplet.graph.size();
      // CSH 1998-02-02 changed getSize to size for 1.0 compatibility
      java.awt.Graphics g = theApplet.graph.getGraphics();
      g.setColor(theApplet.graph.getBackground());
      g.fillRect(0, 0, d.width, d.height);
      g.dispose();
      theApplet.repaint();
   }

   static void addShape(Shape s) { theApplet.graph.addShape(s); }

   /**
    * Sets the coordinate system for drawing graphics
    * @param xleft the x coordinate of the left border
    * @param ytop the y coordinate of the top border
    * @param xright the x coordinate of the right border
    * @param ybottom the y coordinate of the bottom border
    */

   public void setCoord(double xleft, double ytop, double xright, double ybottom)
   {  graph.setCoord(xleft, ytop, xright, ybottom);
   }

   private Thread runner;
   private Point clicked;
   private java.awt.TextField textbox;
   private GraphicsCanvas graph;
   private String text;
   private java.awt.Label label;
   private String tracking;
   GraphicsCoord coord;

   private static GraphicsApplet theApplet;
}

class GraphicsCanvas extends java.awt.Canvas
{  public GraphicsCanvas()
   {  shapes = new java.util.Vector();
      coord = new GraphicsCoord();
   }

   public void paint(java.awt.Graphics g)
   {  for (int i = 0; i < shapes.size(); i++)
         ((Shape)shapes.elementAt(i)).redraw(g, coord);
   }

   public void reshape(int x, int y, int w, int h)
   {  int s = Math.min(w, h);
      x += (w - s) / 2;
      y += (h - s) / 2;
      super.reshape(x, y, s, s);
      coord.setPixel(size().width, size().height);
   }

   public void setCoord(double xleft, double ytop, double xright, double ybottom)
   {  coord.setCoord(xleft, ytop, xright, ybottom);
   }


   Point getPointFromPixelPosition(int x, int y)
   {  return new Point(coord.xFromPixelPos(x),
         coord.yFromPixelPos(y));
   }


   void addShape(Shape s)
   {  shapes.addElement(s.clone());
      s.redraw(getGraphics(), coord);
   }

   GraphicsCoord coord;
   static java.util.Vector shapes;
}











