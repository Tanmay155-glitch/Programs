//Create a Java program using a while loop to calculate the sum of integers from 1 to 100
public class Q5
{
    public static void main(String[] args)
    {
        int sum=0;
        for(int i=1;i<=100;i++)
        {
            sum+=i;
        }
        System.out.println("Sum of First 100 numbers are: "+sum);
    }
}