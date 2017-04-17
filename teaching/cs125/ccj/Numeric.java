/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Numeric.java
****************************************************************************/

/**
 * The Numeric class provides useful numeric functions 
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;

public class Numeric
{  /**
    * Converts a string to a floating point number. For example, <tt>Numeric.parseDouble("0.5")</tt> returns <tt>0.5</tt>
    * @param s the string to parse
    * @return the floating point value represented by the string.
    */

   public static double parseDouble(String s)
   {  return new Double(s).doubleValue();
   }
   
   /**
    * Compares two floating point numbers to see if they are approximately the same
    * @param x a floating point number
    * @param y another floating point number
    * @return 0 if x and y are approximately identical, -1 if x < y and 1 if x > y
    */

   public static int compareDoubles(double x, double y)
   {  double comp = (x - y) / (1 + Math.max(Math.abs(x), Math.abs(y)));
      if (comp < -EPSILON) return -1;
      if (comp > EPSILON) return 1;
      return 0;
   }

   /**
    * Rounds a floating point number to the nearest integer
    * @param x a floating point number
    * @return the nearest integer
    */

   public static int round(double x)
   {  return (int)Math.round(x);
   }

   /**
    * Generates a random integer in a range. For example, <tt>Numeric.randomInt(1, 6)</tt> generates a random roll of a die
    * @param a the low bound of the range
    * @param b the high bound of the range
    * @return a random integer r, a <= r && r <= b
    */

   public static int randomInt(int a, int b)
   {  if (a > b) throw new IllegalArgumentException();
      if (a == b) return a;
      double x = Math.random();
      int n = a + (int)(x * (b - a + 1));
      if (n > b) n = b;
      return n;
   }

   /**
    * Generates a random floating point number in a range. 
    * @param a the low bound of the range (inclusive)
    * @param b the high bound of the range (exclusive)
    * @return a random floating point number r, a <= r && r < b
    */

   public static double randomDouble(double a, double b)
   {  if (a > b) throw new IllegalArgumentException();
      if (a == b) return a;
      return a + (b - a) * Math.random();
   }

   private static final double EPSILON = 1E-12;
}
