/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Time.java
** CHANGES:
   28 Oct 1997       Fixed constructor Time(int,int,int,int,int,int)
                     to use correct month
                     Fixed equals to ignore milliseconds
****************************************************************************/

/**
 * The time class is useful for determining the current time and for measuring the
 * speed of an algorithm
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;

public class Time implements Cloneable
{  /**
    * Constructs a time object representing the current time
    */

   public Time() { date = new java.util.Date(); }

   /**
    * Constructs a time object
    * @param y the year (must be >= 1970)
    * @param m the month
    * @param d the day
    * @param hr the hours
    * @param min the minutes
    * @param sec the seconds
    */

   public Time(int y, int m, int d, int hr, int min, int sec)
   {  date = new java.util.Date(y - 1900, m - 1, d, hr, min, sec);
   }

   /**
    * Gets the year of this time object
    * @return the year of this time object
    */

   public int getYear() { return date.getYear() + 1900; }

   /**
    * Gets the month of this time object
    * @return the month of this time object
    */

   public int getMonth() { return date.getMonth() + 1; }

   /**
    * Gets the day of this time object
    * @return the day of this time object
    */

   public int getDay() { return date.getDate(); }

   /**
    * Gets the hours of this time object
    * @return the hours of this time object
    */

   public int getHours() { return date.getHours(); }

   /**
    * Gets the minutes of this time object
    * @return the minutes of this time object
    */

   public int getMinutes() { return date.getMinutes(); }

   /**
    * Gets the seconds of this time object
    * @return the seconds of this time object
    */

   public int getSeconds() { return date.getSeconds(); }

   /**
    * Adds a number of seconds to this time object 
    * @param s the seconds to add (if < 0, the result is an earlier time)
    */

   public void addSeconds(double s)
   { date = new java.util.Date(date.getTime() + Math.round(1000 * s)); }

   /**
    * Computes the number of seconds between two times
    * @param t2 the other time
    * @return the number of seconds between <tt>t</tt> and <tt>t2</tt>. If < 0, then <tt>t</tt> is after <tt>t2</tt>.
    * 
    */

   public float secondsFrom(Time t2)   
   { return (date.getTime() - t2.date.getTime()) / 1000; }

   /**
    * Tests if this object equals another
    * @param b the object to compare with
    * @return <tt>true</tt> if the two objects are equal
    */

   public boolean equals(Object o2)
   {  if (!(o2 instanceof Time)) return false;
      Time t2 = (Time)o2;
      return date.getTime() / 1000 == t2.date.getTime() / 1000;
   }

   /**
    * Creates a string representation of this object
    * @return a string representation of this object
    */

   public String toString()
   { return "Time[year = " + getYear() + ", month = " + getMonth() + ", day = "
                    + getDay() + ", hours = " + getHours() + ", minutes = " + getMinutes()
                    + ", seconds = " + getSeconds() + "]";
   }

   /**
    * Creates a copy of this object
    * @return a copy of this object
    */

   public Object clone()
   {  try
      {  return super.clone();
      }
      catch(CloneNotSupportedException e)
      {  return null;
      }
   }

   private java.util.Date date;
}








