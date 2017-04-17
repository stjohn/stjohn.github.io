/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Initials.java
**
** Modified to work with SavitchIn.  kas, 9/21/99
****************************************************************************/
import SavitchIn.*;

public class Initials
{  public static void main(String[] args)
   {  
      System.out.print("Please enter your full name "
         + "(first middle last): ");
      String first = SavitchIn.readLineWord();
      String middle = SavitchIn.readLineWord();
      String last = SavitchIn.readLineWord();
      String initials = first.substring(0, 1)
         + middle.substring(0, 1)
         + last.substring(0, 1);

      System.out.println("Your initials are " + initials);
   }
}




