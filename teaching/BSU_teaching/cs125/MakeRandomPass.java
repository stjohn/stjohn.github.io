/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             MakePass.java

** Modified for Exercise P2.23: generate a random password using 
** 	Numeric.randomInt(1, 1000).
****************************************************************************/
import ccj.*;

public class MakeRandomPass
{  public static void main(String[] args)
   {  
      System.out.print("Please enter your full name "
         + "(first middle last): ");
      String first = Console.in.readWord();
      String middle = Console.in.readWord();
      String last = Console.in.readWord();
      String initials = first.substring(0, 1)
         + middle.substring(0, 1)
         + last.substring(0, 1);

      System.out.print("Please enter your age: ");
      int age = Console.in.readInt();
     
      int key = Numeric.randomInt(1,1000) * age;
      key = key % 10000;

      String password = initials.toLowerCase() + key;

      System.out.println("Your password is " + password);
   }
}




