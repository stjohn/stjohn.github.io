/**
 * From _Java in a Nutshell_ by David Flanagan, 
 *      Copyrighted by O'Reilly and Associates, 1996.
 *
 * This program does simple animation.
 */

import java.applet.*;
import java.awt.*;
import java.net.*;
import java.util.*;

public class animate extends Applet implements Runnable
{
    protected Image[] images;	//Array that stores the images
    protected int current_image;//The index of image being displayed

    //Get the name of the images.  Assumes that all the image names
    //begin the same, for example "group", and then loads the pictures
    //group1.jpg, group2.jpg,...  The parameter basename contains
    //the beginning of the name.  The parameter num_images contains
    //the number of images.
    public void init()
    {
    	String basename = this.getParameter("basename");
	int num_images;
	try {
	    num_images = Integer.parseInt(this.getParameter("num_images"));
	}
	catch (NumberFormatException e) {
	    num_images = 0;
	}

	images = new Image[num_images];
	for (int i = 1 ; i <= num_images ; i++)
	{
	    images[i-1] = this.getImage(this.getDocumentBase(), 
	    		basename + i + ".jpg");
	}
    }

    //This is the thread that runs the animation and the 
    //methods that start and stop it:
    private Thread animate_thread = null;

    public void start()
    {
    	if (animate_thread == null)
	{
	    animate_thread = new Thread(this);
	    animate_thread.start();
	}
    }

    public void stop()
    {
    	if ((animate_thread != null) && animate_thread.isAlive())
	{
	    animate_thread.stop();
	}

	//Set to null, so, it can be picked up by garbage collection
	animate_thread = null;
    }

    //Here's what the thread does:
    public void run()
    {
    	while (true)
	{
	    current_image++;
	    if (current_image == images.length)
	    	current_image = 0;
	    this.getGraphics().drawImage(images[current_image],0,0,this);
	    try {
	    	Thread.sleep(500);
	    }
	    catch (InterruptedException e) { ; }
	}
    }

}


