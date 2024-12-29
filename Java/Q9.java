// Create a method that accepts an array and returns the maximum value using a for loop
public class Q9
{
    public static int findmax(int[] array)
    {
        int max=array[0];
        for(int i=1;i<array.length;i++)
        {
            if(array[i]>max)
            {
                max=array[i];
            }
        }
        return max;
    }
    public static void main(String args[])
    {
        int[] number = {1, 2, 3, 4, 5, 6, 7};
        int max=findmax(number);
        System.out.println("Maximum number: " + max);
    }
}