import java.util.Scanner;
public class Age
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter your Age:");
        int x=s.nextInt();
        if(x<18)
        {
            System.out.println("You are Minor");
        }
        else if(x>=18)
        {
            System.out.println("You Adult");
        }
        else
        {
            System.out.println("Enter Valid Value");
        }
    }
}