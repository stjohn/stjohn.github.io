/****************************************************************************
** COPYRIGHT (C):    1996 Cay S. Horstmann. All Rights Reserved.
** PROJECT:          Computing Concepts with Java
** FILE:             Employee.java
****************************************************************************/

/**
 * An employee class that is used for many examples in the book
 * @version 1.00 11 Apr 1997
 * @author Cay Horstmann
 */

package ccj;

public class Employee implements Cloneable
{  /**
    * Constructs an employee object
    * @param n the employee name
    * @param s the employee salary
    */

   public Employee(String n, double s) { name = n; salary = s; }

   /**
    * Default constructor
    */
  
   public Employee() { name = ""; salary = 0; } /* CSH 1998-02-28 */

   /**
    * Gets the employee name
    * @return the employee name
    */

   public String getName() { return name; }

   /**
    * Gets the employee salary
    * @return the employee salary
    */

   public double getSalary() { return salary; }

   /**
    * Sets the employee salary
    * @param s the new salary
    */

   public void setSalary(double s) { salary = s; }

   /**
    * Tests if this object equals another
    * @param b the object to compare with
    * @return <tt>true</tt> if the two objects are equal
    */

   public boolean equals(Object ob)
   {  if (!getClass().equals(ob.getClass())) return false;
      Employee b = (Employee)ob;
      return name.equals(b.name) && salary == b.salary;
   }

   /**
    * Creates a string representation of this object
    * @return a string representation of this object
    */

   public String toString()
   { return "Employee[name = " + name + ", salary = " + salary + "]";
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

   private String name;
   private double salary;
}

