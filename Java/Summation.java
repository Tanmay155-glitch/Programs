import java.util.Scanner;
public class Summation
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the N number for the summation: ");
        int n=s.nextInt();
        int sum=0;
        for(int i=0;i<=n;i++)
        {
            sum=sum+i;
            System.out.println(sum);
        }
        System.out.println("Summation of "+n+" is :"+sum);
    }
}