/**
 * An employee class from lecture on 18 October.  We keep
 * track of name, address, salary, and social security number.
 * We'll add more to this class (for example, constructors)
 * in later versions.
 **/

public class Employee 
{  

    public String name;
    public String address;
    public int phone;
    public int SSN; 
    private double salary;

   /**
    * Prints the employee information
    **/

    public void print() 
    { 
        System.out.println(name + "\n"
               + address + "\n" + phone);
    }

   /**
    * Prints the social security number and salary.
    **/

    public void printPrivate() 
    { 
        System.out.println(SSN + "\n$" + salary);  
    }

   /**
    * Gets the employee salary
    * @return the employee salary
    **/

    public double getSalary() 
    { 
        return salary; 
    }

   /**
    * Sets the employee salary
    * @param s the new salary
    **/

    public void setSalary(double s) 
    { 
        salary = s; 
    }

}

