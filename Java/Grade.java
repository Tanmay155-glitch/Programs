import java.util.Scanner;
public class Grade
{
    public static void main(String args[])
    {
        Scanner s=new Scanner(System.in);
        int marks=0;
        int max=0;
        int sum=0;
        int count=0;
        int avg=0;
        System.out.println("Enter the Grasdes of Student");
        while(true)
        {
            marks=s.nextInt();
            ++count;
            if(marks>max)
            {
                max=marks;
            }
            sum=marks+sum;
            if(marks==-1)
            {
                avg=sum/count;
                System.out.println("Average Marks: "+avg);
                System.out.println("Sum is: "+sum);
                System.out.println("Highest Marks: "+max);
                break;
            }
        }
    }
}