import java.util.Scanner;
public class AddEven
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the Starting value of Even number:");
        int start=s.nextInt();
        System.out.println("Enter the ending value of Even Number:");
        int end=s.nextInt();
        int sum=0;
        for(int i=start;i<=end;i++)
        {
            if(i%2==0)
            {
                sum=sum+i;
                System.out.println(sum);
            }
        }
        System.out.println("Summantion of Even number from "+start+" to "+end+" is "+sum);
    }
}