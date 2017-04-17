/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Coins1.java
****************************************************************************/

public class Coins1
{   public static void main(String[] args)
    {  int pennies = 8;
	    int dimes = 4;
	    int quarters = 3;

	    double total = pennies * 0.01 + dimes * 0.10
         + quarters * 0.25;
       /* total value of the coins */

       System.out.println(total);
	}
}







