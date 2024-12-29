//Write a program that prints the multiplication table for a given number. The user should input the number and the range (e.g., up to 10 or 20). Use a for loop to generate the table.
import java.util.Scanner;
public class Q23
{
    public static void main(String[] args)
    {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter the number you want table(1 to 20): ");
        int n=s.nextInt();
        if(n<=20)
        {
            for(int i=1;i<=10;i++)
            {
                System.out.println(n+" X "+i+"= "+(n*i));
            }
        }
        else
        {
            System.out.println("Enter the number below 20");
        }
    }
}