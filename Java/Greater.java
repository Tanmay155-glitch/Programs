import java.util.Scanner;
public class Greater
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter First Value: ");
        int a=s.nextInt();
        System.out.println("Enter Second value: ");
        int b=s.nextInt();
        System.out.println("Enter Third Value: ");
        int c=s.nextInt();
        if(a>b && a>c)
        {
            System.out.println("Value of a is greater a: "+a);
        }
        else if(b>a && b>c)
        {
            System.out.println("Value of b is graeter b: "+b);
        }
        else if(c>a && c>b)
        {
            System.out.println("Value of c is greater c: "+c);
        }
        else
        {
            System.out.println("Enter Valid value");
        }
    }
}