
import ccj.*;

public class Manager extends GraphicsApplet
{
    public void run()
    {
	Track t = new Track();
	
	for (int i=0 ; i < 100 ; i++)
	{
	    t.drive();
	    t.draw();
	}
    } 
}
