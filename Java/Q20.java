//Program prints numbers from 1 to 10 but skips the number 5.
public class Q20
{
    public static void main(String[] args)
    {
        for(int i=1;i<=10;i++)
        {
            if(i==5)
            {
                continue;
            }
            System.out.println(i);
        }
    }
}