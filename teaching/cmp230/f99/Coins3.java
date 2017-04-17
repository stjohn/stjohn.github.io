/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Coins3.java
****************************************************************************/

import ccj.*;

public class Coins3
{  public static void main(String[] args)
   {  System.out.print("How many pennies do you have? ");
      int pennies = Console.in.readInt();
      System.out.print("How many nickels do you have? ");
      int nickels = Console.in.readInt();
      System.out.print("How many dimes do you have? ");
      int dimes = Console.in.readInt();
      System.out.print("How many quarters do you have? ");
      int quarters = Console.in.readInt();

      double total = pennies * 0.01 + nickels * 0.05 +
            dimes * 0.10 + quarters * 0.25;
      /* total value of the coins */

      System.out.println("Total value = " + total);
   }
}


