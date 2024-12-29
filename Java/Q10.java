//Write a Java program that finds the average of numbers stored in an integer array.
public class Q10
{
    public static void main(String[] args)
    {
        int[] array = {10,20,30,40,50};
        int sum=0;
        float avg=0.0f;
        for(int i = 0; i < array.length; i++)
        {
            sum+=array[i];
        }
        avg=sum/array.length;
        System.out.println("Average: " + avg);
    }
}