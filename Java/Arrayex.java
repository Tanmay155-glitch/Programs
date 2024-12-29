import java.util.Scanner;
public class Arrayex
{
    public static void main(String args[])
    {
        int[] m=new int[5];
        int sum=0;
        int avg=0;
        Scanner sc=new Scanner(System.in);
        for(int i=0;i<=4;i++)
        {
            System.out.println("Enter the marks of Subject "+i+" :");
            m[i]=sc.nextInt();
        }
        for(int i=0;i<=4;i++)
        {
            sum=sum+m[i];
        }
        avg=sum/5;
        System.out.println("Total of all Subject is: "+avg);
        System.out.println("Average is: "+avg);
    }
}