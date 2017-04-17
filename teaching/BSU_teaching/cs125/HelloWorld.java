  //The HelloWorld class implements an applet that
  //simply paints "Hello World!".

  import java.applet.Applet; //Include applet class, so, we can use on webpage
  import java.awt.Graphics;  //Include graphics, so, we can "paint" the message

  public class HelloWorld extends Applet {      //Needed to make the applet
       public void paint(Graphics g) {          //Tells the class what to 
              g.drawString("Hello world!", 50, 25);    //paint to the screen
       }
  }
