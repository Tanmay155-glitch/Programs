//Create a while loop that prompts the user for their flight choice until a valid number is entered
import java.util.Scanner;
public class Q2
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        while (true)
        {
            System.out.println("Enter the Flight Number:");
            int flight=s.nextInt();
            if(flight>0)
            {
                System.out.println("Valid Flight Choice: "+flight); 
                break;
            }
            if(flight<=0)
            {
                System.out.println("Invalid Flight Choice: "+flight);
            } 
        }
    }
}