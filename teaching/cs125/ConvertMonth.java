/****************************************************************************
** This program takes the number representing a month and 
** prints out the corresponding word:  
** 	for example, for 3, we print March.
** 
** Solution to P2.22 on p 81.
**
****************************************************************************/
import ccj.*;

public class ConvertMonth
{  public static void main(String[] args)
   {  
      /* Store the names of the months in a long string that
       * has 10 characters per month: */
      String monthNames =  "January   " + "February  "
          + "March     " + "April     " + "May       "
          + "June      " + "July      " + "August    "
          + "September " + "October   " + "November  "
          + "December  ";

      System.out.print("Please enter the number of the month "
         + "(1-12): ");
      int monthNum = Console.in.readInt();
      String desiredName = monthNames.substring(
		(monthNum-1)*10, monthNum*10);

      System.out.print("The month is " + desiredName +"\n");
   }
}




