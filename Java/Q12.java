//Demonstrate how to find the minimum and maximum values in a given array.
public class Q12
{
    public static void main(String[] args)
    {
        int[] array = {1, 2, 3, 4, 5, 6, 7};
        int max=array[0];
        int min=array[0];
        for(int i = 0; i < array.length; i++)
        {
            if(max<array[i])
            {
                max=array[i];
            }
        }
        System.out.println(max);
        for(int i = 0; i < array.length; i++)
        {
            if(min>array[i])
            {
                min=array[i];
            }
        }
        System.out.println(min);
    }
}