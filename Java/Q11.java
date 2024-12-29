//Write a Java program that sums the elements of a 2D array
public class Q11
{
    public static void main(String[] args)
    {
        int[][] array={{10,20,30},{40,50,60}};
        int sum=0;
        for (int i=0; i<array.length; i++)
        {
            for(int j=0;j<array[i].length; j++)
            {
                sum+=array[i][j];
            }
        }
        System.out.println("sum: " + sum);
    }
}