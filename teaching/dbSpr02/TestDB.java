import java.sql.*;

public class TestDB
{
    public static void main(String[] args)
    {

	//Implicitly load the driver:
	//  This could throw a ClassNotFoundException that should 
	//  be caught:
	try {
	    Class.forName("postgresql.Driver");
	}
	catch(Exception e)
	{
	    System.out.println(e);
	    System.exit(1);
	}

	System.out.println("Test successful.");
	
    }
}

