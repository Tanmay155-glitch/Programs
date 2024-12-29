//Design a Java program that merges two sorted arrays into a single sorted array
public class Q13 
{
    public static void main(String[] args) 
    {
        int[] array1 = {1, 3, 5, 7, 9};
        int[] array2 = {2, 4, 6, 8, 10};

        int[] mergedArray = new int[array1.length + array2.length];

        int i = 0, j = 0, k = 0;

        for (; i < array1.length && j < array2.length; k++) 
        {
            if (array1[i] < array2[j]) 
            {
                mergedArray[k] = array1[i];
                i++;
            } 
            else 
            {
                mergedArray[k] = array2[j];
                j++;
            }
        }

        for (; i < array1.length; i++, k++) 
        {
            mergedArray[k] = array1[i];
        }

        for (; j < array2.length; j++, k++) 
        {
            mergedArray[k] = array2[j];
        }

        System.out.println("Merged Sorted Array: ");
        for (int num : mergedArray) 
        {
            System.out.print(num + " ");
        }
    }
}
