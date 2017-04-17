/* This program uses the class Employee, written in lecture
   on 18 October.
   It demostrates how to create an object, access public
   member variables and use member functions.
 */

import SavitchIn.*;

public class testEmployee
{
    public static void main(String args[])
    {
        // Declare some variables, including 2 of type Employee
        Employee Boss;
        double currentSal = 0;
        Employee Angel = new Employee(); //get space to store
                 //info about Angel-- for objects, you need to 
                 //use "new" to get space for all the members
                 //You can do this in one line, or split:
        Boss = new Employee(); 

        //Set up info about Angel and print:
        Angel.name = "Angel M.";
        Angel.phone = 5551212;
        Angel.print();
        System.out.println();

        //Set up info about boss, and print:
        Boss.name = "Bill Clinton";
        Boss.address = "1600 Pennsylvania Ave., D.C.";
        Boss.SSN = 123456789;
        Boss.phone = 5555555;
        Boss.setSalary(200000);
        Boss.print();
        Boss.printPrivate();
        System.out.println();

        //Give the boss a 10% raise and print:
        currentSal = Boss.getSalary();
        double newSalary = currentSal*1.1;
        Boss.setSalary(newSalary);
        Boss.print();
        Boss.printPrivate();
        System.out.println();

        //To keep the window up in JBuilder:
        System.out.print("Hit return to quit");
        String junk = SavitchIn.readLine();
    }
}
