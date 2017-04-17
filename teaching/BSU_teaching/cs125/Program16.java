
/* 
 * This file demonstrates the features of the Person
 * class.
 */

import ccj.*;

public class Program16 
{
  public static void main(String args[])
  {
    String answer;

    do 
    {
      Person george = new Person("George", "Smith");
      System.out.println( "\ngeorge's name is " + george.getFirstName()
        + " " + george.getLastName());

      george.setLastName("George");
      george.setFirstName("Smith");
      System.out.println( "\ngeorge's new info is\n" + george);
	
      Person fred = new Person();
      System.out.println( "\nfred's info: " + fred.getFirstName()
        + " " + fred.getLastName() + " " + fred.getBday());

      System.out.print( "\nEnter a first name: ");
      String first = Console.in.readWord();
      System.out.print( "Enter a last name: ");
      String last = Console.in.readWord();

      System.out.print( "Enter the year of birth: ");
      int year = Console.in.readInt();
      System.out.print( "Enter the month of birth: ");
      int month = Console.in.readInt();
      System.out.println( "Enter the day of birth: ");
      int day = Console.in.readInt();
	
      Time bday = new Time(year, month, day, 0, 0, 0);
      fred = new Person(first, last, bday);
	    
      System.out.println( "\nfred's new info is " + fred);

      System.out.print("\nDo you want to enter information again? ");
      answer = Console.in.readWord();
    }
    while ( answer.substring(0,1).toUpperCase().equals("Y") );
  }
}
