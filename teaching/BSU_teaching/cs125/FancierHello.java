  //The HelloWorld class implements an applet that
  //simply paints "Hello World!".

  import java.applet.Applet; //Import applet class, so, we can use on webpage
  import java.awt.*;         //Import windows toolkit

  public class FancierHello extends Applet {      //Needed to make the applet

    // init() contains everything that should be done once,
    // when the applet begins.  For example, here is where we
    // set the font size.

    public void init()
    {
        font = new Font("Helvetica", Font.BOLD, 48);
    }
   
    // Tells the class what to paint to the screen
    public void paint(Graphics g) {          

        Rectangle r = this.bounds();
        g.setColor(Color.blue);
        g.fillRect(r.x, r.y, r.width, r.height);
        g.setColor(Color.black);
        g.drawRect(5,25,280,100);

        g.setColor(Color.darkGray);
        g.setFont(font);
        g.drawString(message, 10,100);    
    }

    static final String message = "Hello World";
    private Font font;
  }

