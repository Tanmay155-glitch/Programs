import java.util.Scanner; //This Package is used to take the input from user
public class ATM
{
    public static void main(String args[])//Main Method of java Program it is compilser to write in code
    {
        Scanner s=new Scanner(System.in);//We create scanner that is used to take input in program of Any data type like int,String,float,double,char,etc.
        int balance=5000;//Set the balance in the account of the user 
        while(true)//used for repatedly looping until the user choose Exit or break the loop
        {
            System.out.println("Choose:\n1 : Check Balance \n2 : Credit  \n 3 : Withdraw \n4 : Exit");
            int x=s.nextInt();
            switch(x)//used for checking multiple condition 
            {
                case 1: //In this Case We display the balance of the user
                    System.out.println("Balance is: "+balance);
                    break;
                case 2: //In this Case we have to add the amount in the bank
                    System.out.println("Enter the amount you want to Credit: ");
                    int c=s.nextInt();
                    balance=balance+c;
                    System.out.println("Current Amount is: "+balance);
                break;
                case 3: //In this Case we have to withdraw the amount form the bank
                    System.out.println("Enter the amount you want to withdraw: ");
                    int w=s.nextInt();
                    balance=balance-w;
                    System.out.println("Current Balance is: "+balance);
                break;
                case 4: //This Case is used to Exit the loop
                    System.exit(0);
                break;
                default:
                    System.out.println("Choose the Valid Operation");
                break;
            }
        }
    }
}