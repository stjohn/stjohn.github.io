/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Console.java
****************************************************************************/

/**
 * 
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;

public class Console
{ /**
   *  The standard text input stream, like <tt>System.in</tt>, but with methods for reading numeric input
   */
   public static TextInputStream in
        = new TextInputStream(java.lang.System.in, java.lang.System.out);
  /**
   *  The standard text output stream, like <tt>System.out</tt>, but with methods for formatted output
   */
   public static TextOutputStream out
        = new TextOutputStream(java.lang.System.out);
}





