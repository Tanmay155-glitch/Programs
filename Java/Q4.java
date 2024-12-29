//Write a Java program that uses a for loop to print the first 10 numbers of the Fibonacci sequence.
public class Q4
{
    public static void main(String[] args)
    {
        int n1=0, n2=1;
        System.out.println("Fibonacci Series from 1 to 10");
        for(int i=1;i<=10;i++)
        {
            System.out.println(n1);
            int next=n1+n2;
            n1=n2;
            n2=next;
        }
    }
}