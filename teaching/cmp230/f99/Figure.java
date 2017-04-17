
/*****************************************************************
 *Class for simple character graphics figures to send to screen.
 *This class can draw an asterisk on the screen as a test. But,
 *it is not intended to be a figure used in graphics. 
 *It is intended to be used as a base class for the kinds
 *of figures that will be used in graphics applications. 
 ****************************************************************/
public class Figure
{
    public Figure()
    {
        offset = 0; 
    }
    
    public Figure(int theOffset)
    {
        offset = theOffset;
    }
   
    public void resetOffset(int newOffset)
    {
        offset = newOffset;
    }
   
    public int offsetValue()
    {
        return offset;
    }
        
      
    /*******************************************
     *Draws the figure at lineNumber lines down
     *from the current line.
     *******************************************/     
    public void drawAt(int lineNumber)
    {
        int count;
        for (count = 0; count < lineNumber; count++)
            System.out.println(); 
        drawHere();
    } 

    /********************************************
     *Draws the figure at the current line.
     ********************************************/      
    public void drawHere()
    {
        int count;
        for (count = 0; count < offset; count++)
            System.out.print(' ');
        System.out.println('*');
    }
    
    private int offset; 
}


