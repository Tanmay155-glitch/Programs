//Find the first even number in a list and breaks the loop when it finds.
public class Q16
{
    public static void main(String[] args)
    {
        int[] array={3,4,5,6,7,8,9,2,1};
        System.out.println("Even number in array: ");
        for (int i = 0; i < array.length; i++)
        {
            if(array[i]%2==0)
            {
                System.out.println(array[i]);
            }
        }
    }
}