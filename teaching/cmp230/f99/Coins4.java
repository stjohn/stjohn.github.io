/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Coins4.java
****************************************************************************/

import ccj.*;

public class Coins4
{  public static void main(String[] args)
   {  System.out.print("How many pennies do you have? ");
      int count = Console.in.readInt();
      double total = count * 0.01;
      System.out.print("How many nickels do you have? ");
      count = Console.in.readInt();
      total = total + count * 0.05;
      System.out.print("How many dimes do you have? ");
      count = Console.in.readInt();
      total = total + count * 0.10;
      System.out.print("How many quarters do you have? ");
      count = Console.in.readInt();
      total = total + count * 0.25;

		System.out.println("Total value = " + total);
   }
}





