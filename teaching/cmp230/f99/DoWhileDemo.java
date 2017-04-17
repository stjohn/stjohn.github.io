public class DoWhileDemo
{
    public static void main(String[] args)
    {
        int count, number;

        System.out.println("Enter a number");
        number = SavitchIn.readLineInt();

        count = 1;
        do
        {
            System.out.print(count + ", ");
            count++;
        }while (count <= number);
        System.out.println();
        System.out.println("Buckle my shoe.");
    }
}

