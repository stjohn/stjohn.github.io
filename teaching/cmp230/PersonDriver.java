import java.util.Scanner;

/* A driver for the Person class that demonstrates
 * some of its methods.
 */

public class PersonDriver {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Person joe = new Person();
		Scanner scan = new Scanner(System.in);
		String fname, lname;
		int phone;
		
		System.out.print("Default constructor: ");
		System.out.println(joe.getFirstName() + " " + joe.getLastName());
		
		System.out.print("\nPlease enter your first name: ");
		fname = scan.next();
		System.out.print("Please enter your last name: ");
		lname = scan.next();
		
		Person you = new Person(fname, lname);
		
		System.out.println("You entered: " + you.toString());
		
		System.out.print("Please enter your 7-digit phone number: ");
		phone = scan.nextInt();
		you.setPhone(phone);
		System.out.println("You entered: " + you.toString());
		
		System.out.print("\nPlease enter your first name: ");
		fname = scan.next();
		System.out.print("Please enter your last name: ");
		lname = scan.next();
		System.out.print("Please enter your 7-digit phone number: ");
		phone = scan.nextInt();
		
		Person me = new Person(fname, lname, phone);
		
		System.out.println("You entered: ");
		System.out.println("\tfirst name: "+ me.getFirstName());
		System.out.println("\tlast name: "+ me.getLastName());
		System.out.println("\tphone number: "+me.getPhone());
	}

}
