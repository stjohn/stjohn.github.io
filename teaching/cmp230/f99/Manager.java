/**
 * The Manager class from lecture on 29 November.  The class
 * extends the Employee class.  It also has a list of underlings
 * for the manager, a constructor, and a new methods to change
 * and access the list of employees.
 **/

public class Manager extends Employee 
{  
    private int numEmployees;  //Keeps track of number of underlings
    private Employee[] underlings = new Employees[10];
                               //Assume at most 10 employees per 
                               //manager

   /**
    * Default Constructor:  Sets up manager and underlings
    **/
    public Manager()
    {
        super();    //Call the constructor from the super class (Employee)
        numEmployees = 0;
    }

   /**
    * Read in the manager information and the list of underlings:
    **/
    public void read() 
    {
        //Read in information about manager
        //Get number of employees:
        //Read in information about each employee:
    }

   /**
    * Prints the employee information and the list of underlings:
    **/

    public void print() 
    { 
        super.print();

        System.out.println("Employees:\n");
        int i;
        for ( i = 0 ; i < numEmployees ; i++ )
        {
             underlings[i].print();
        }       
 
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

