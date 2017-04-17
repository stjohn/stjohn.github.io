/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Coins5.java
****************************************************************************/

import ccj.*;

public class Coins5
{  public static void main(String[] args)
   {  System.out.print("How many pennies do you have? ");
      int pennies = Console.in.readInt();
      System.out.print("How many nickels do you have? ");
      int nickels = Console.in.readInt();
      System.out.print("How many dimes do you have? ");
      int dimes = Console.in.readInt();
      System.out.print("How many quarters do you have? ");
      int quarters = Console.in.readInt();

      int value = pennies + 5 * nickels
         + 10 * dimes + 25 * quarters;
      int dollar = value / 100;
    	int cents = value % 100;

      System.out.println("Total value = " + dollar
         + " dollar and " + cents + " cents");
   }
}



