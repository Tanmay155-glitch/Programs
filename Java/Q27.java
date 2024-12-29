//You are tasked with developing a program that tracks a user's monthly expenses. The program should repeatedly ask the user to input their expenses for different categorie (like food, transportation, etc.) until they type "done". After the user is finished, display the total expenses for the month.
import java.util.Scanner;

public class Q27 
{
    public static void main(String[] args) 
    {
        Scanner scanner = new Scanner(System.in);
        double totalExpenses = 0.0;

        System.out.println("Monthly Expenses Tracker (INR)");
        System.out.println("Type 'done' to finish.");

        while (true) 
        {
            System.out.print("Enter expense amount (or type 'done'): ");
            String input = scanner.nextLine();

            if (input.equalsIgnoreCase("done") || input.equalsIgnoreCase("Done")) 
            {
                break;
            }

            try 
            {
                double amount = Double.parseDouble(input);
                totalExpenses += amount;
                System.out.println("Added ₹" + amount);
            } 
            catch (NumberFormatException e) 
            {
                System.out.println("Invalid input. Please enter a valid amount.");
            }
        }

        System.out.println("\nTotal Expenses for the Month: ₹" + totalExpenses);
    }
}