/**
 * A modified version of the employee class (from lecture on 
 * 18 October), discussed in class on 8 November.  We keep
 * track of name, address, salary, and social security number.
 * We've added to contructors, to initialize objects, to this
 * class.
 **/

public class Employee2 
{  

    public String name;
    public String address;
    public int phone;
    public int SSN; 
    private double salary;

   /**
    * Default Constructor
    **/
    public Employee2()
    {
        name = "unknown";
        address = "unknown";
        phone = 0; SSN = 0; salary = 0; 
    }

   /**
    * Constructor, given name and address:
    **/
    public Employee2(String new_name, int new_ssn)
    {
        name = new_name;
        address = "unknown";
        SSN = new_ssn; 
        phone = 0; 
        salary = 0; 
    }

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

