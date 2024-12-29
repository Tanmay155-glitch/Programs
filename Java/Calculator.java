import java.util.Scanner;
public class Calculator
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter First Value: ");
        int a=s.nextInt();
        System.out.println("Enter Second value: ");
        int b=s.nextInt();
        int c;
        System.out.println("Select the operation:");
        System.out.println("1: Addition \n 2: Subtraction \n 3: Division \n 4: Multiplication");
        int n=s.nextInt();
        switch(n)
        {
            case 1:
                c=a+b;
                System.out.println("Addition is: "+c);
            break;
            case 2:
                c=a-b;
                System.out.println("Subtraction is: "+c);
            break;
            case 3:
                c=a/b;
                System.out.println("Division is: "+c);
            break;
            case 4:
                c=a*b;
                System.out.println("Multiplication is: "+c);
            break;
        }
    }
}