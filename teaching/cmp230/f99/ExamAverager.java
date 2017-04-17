/*********************************************************************
 *Determines the average of a list of (nonnegative) exam scores.
 *Repeats for more exams, until the user says she/he is finished.
 *****************************************************************/
public class ExamAverager
{
    public static void main(String[] args)
    {
        System.out.println("This program computes the average of");
        System.out.println("a list of (nonnegative) exam scores.");

        double sum;
        int numberOfStudents;
        double next;
        char answer;

        do
        {
            System.out.println();
            System.out.println("Enter all the scores to be averaged.");
            System.out.println("Enter a negative number after");
            System.out.println("you have entered all the scores.");

            numberOfStudents = 0;
            next = SavitchIn.readLineDouble();
            while (next >= 0)
            {
                sum = sum + next;
                numberOfStudents++;
                next = SavitchIn.readLineDouble();
            }
            if (numberOfStudents > 0)
                 System.out.println("The average is " 
                                     + (sum/numberOfStudents));
           else
                System.out.println("No scores to average.");

            System.out.println("Want to average another exam?");
            System.out.println("Enter y for yes or n for no.");
            answer = SavitchIn.readLineNonwhiteChar();
        }while ((answer == 'y') || (answer == 'Y'));
    }
}


