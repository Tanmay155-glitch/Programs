//As part of a feedback collection system, you want to gather customer ratings for a product. Design a program that prompts customers to rate the product from 1 to 5. Usea labeled while loop to continue collecting ratings until a customer enters 0. After collecting all ratings, compute and display the average rating and the number of ratings received.
import java.util.Scanner;
public class Q26
{
    public static void main(String[] args)
    {
        Scanner s=new Scanner(System.in);
        int c=0,r=0,sum=0;
        float avg=0.0f;
        while(true)
        {
            System.out.println("Enter the Product Rating from 1 to 5: ");
            r=s.nextInt();
            if(r>5)
            {
               break; 
            }
            else
            {
                if(r==0)
                {
                    break;
                }
                c++;
                sum+=r;
            }
        }
        avg=sum/c;
        System.out.println("Count of Rates: "+c);
        System.out.println("Average of the Rates: "+avg);
    }
}