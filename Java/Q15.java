//Find the Second largest element in Java
public class Q15
{
    public static void main(String[] args) 
    {
        int[] array = {12, 35, 1, 10, 34, 1};
        
        int firstLargest = Integer.MIN_VALUE;
        int secondLargest = Integer.MIN_VALUE;
        
        for (int num : array) 
        {
            if (num > firstLargest) 
            {
                secondLargest = firstLargest;
                firstLargest = num;
            } 
            else if (num > secondLargest && num != firstLargest) 
            {
                secondLargest = num;
            }
        }
        
        System.out.println("Second largest element is: " + secondLargest);
    }
}
