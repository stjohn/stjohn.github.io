public class WhileDemo
{
    public static void main(String[] args) 
    {
        int count, number;

        System.out.println("Enter a number");
        number = SavitchIn.readLineInt(); 
        
        count = 1;
        while (count <= number)
        {
            System.out.print(count + ", ");
            count++;
        }
        System.out.println();
        System.out.println("Buckle my shoe.");
    } 
}
