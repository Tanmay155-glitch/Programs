import java.util.Scanner;
public class Ex
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        int correct=12345;
        while(true)
        {
            System.out.println("Enter the Correct password: ");
            int pass=s.nextInt();
        
            if(pass==correct)
            {
                System.out.println("Access Granted!");
                System.exit(0);
            }   
            else
            {
                System.out.println("Incorrect Password");
            }
        }
    }
}