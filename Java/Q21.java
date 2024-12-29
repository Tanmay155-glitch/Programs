//Develop a program that checks whether a given number is prime or not. Use a for loop to test divisibility. If the number is found to be divisible by any number other than 1 and itself, it is not prime.
import java.util.Scanner;

public class Q21 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int number = scanner.nextInt();
        
        boolean isPrime = number > 1;
        for (int i = 2; i <= number / 2; i++) 
        {
            if (number % i == 0) 
            {
                isPrime = false;
                break;
            }
        }
        
        if (isPrime) 
        {
            System.out.println(number + " is a prime number.");
        } 
        else 
        {
            System.out.println(number + " is not a prime number.");
        }
        
    }
}
