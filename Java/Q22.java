//Create a program that reverses the digits of a given integer. Use a while loop to extract each digit and build the reversed number.
import java.util.Scanner;
public class Q22
{
    public static void main(String[] args)
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the number: ");
        int n=s.nextInt();
        int reverse=0;
        while(n!=0)
        {
            int digit=n%10;
            reverse=reverse*10+digit;
            n/=10;
        }
        System.out.println("Reverse number is: "+reverse);
    }
}