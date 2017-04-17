
public class GraphicsDemo
{
    public static final int indent = 5;
    public static final int topWidth = 21;
    public static final int bottomWidth = 4;
    public static final int bottomHeight = 4;
    
    public static void main(String[] args)
    {
        System.out.println("        Save The Redwoods!");

        Triangle top = new Triangle(indent, topWidth);
        Box base = new Box(indent + (topWidth/2) - (bottomWidth/2),
                                            bottomHeight, bottomWidth); 
        top.drawAt(1);
        base.drawAt(0);
    }
}

