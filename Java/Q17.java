//Prints all odd numbers from 1 to 20, using continue to skip even numbers.
public class Q17
{
    public static void main(String[] args)
    {
        System.out.printnl("Odd numbers: ");
        for(int  i=1;i<=20;i++)
        {
            if(i%2==0)
            {
                continue;
            }
            System.out.println(i);
        }
    }
}