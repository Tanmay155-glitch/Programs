//Write a Java program that demonstrates the use of the continue statement in a loop
public class Q7
{
    public static void main(String[] args)
    {
        for(int i=0;i<=10;i++)
        {
            if(i==3)
            {
                continue;
            }
            System.out.println(i);
        }
    }
}