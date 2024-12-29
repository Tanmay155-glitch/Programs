//Prints a multiplication table but skips the multiplication by 5.
import java.util.Scanner;
public class Q18
{
    public static void main(String[] args)
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the table you want: ");
        int n=s.nextInt();
        for(int i=1;i<=10;i++)
        {
            if(i==5)
            {
                continue;
            }
            System.out.println(n+" X "+i+" = "+(n*i));
        }
    }
}