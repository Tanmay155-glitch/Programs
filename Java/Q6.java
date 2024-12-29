//Implement a do-while loop that prompts the user to enter a number until they enter a negative number.
import java.util.Scanner;
public class Q6
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        do
        {
            System.out.println("Enter a number: ");
            int num=s.nextInt();
            if(num<0)
            {
                break; 
            }
            if(num>0)
            {
                System.out.println(num);
            }
        }while(true);
    }
}
