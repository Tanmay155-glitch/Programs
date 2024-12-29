/*Print the Pattern as per given etc
1 1 1 1 1
1 1 1 1
1 1 1
1 1
1 */
public class Q25
{
    public static void main(String[] args)
    {
        for(int i=0;i<5;i++)
        {
            for(int j=i;j<5;j++)
            {
                System.out.print("1");
            }
            System.out.println();
        }
    }
}