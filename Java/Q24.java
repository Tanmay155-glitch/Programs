//Write a program that counts the number of vowels and consonants in a given string. Use a for loop to iterate through the string and keep track of the counts.
import java.util.Scanner;
public class Q24
{
    public static void main(String[] args)
    {
        Scanner s=new Scanner(System.in);
        System.out.println("Enter the String: ");
        String str=s.nextLine();
        int v=0;
        int c=0;
        for(int i=0;i<str.length();i++)
        {
            char ch=str.charAt(i);
            if(ch=='a' || ch=='e' || ch=='i' || ch=='o' || ch=='u' || ch=='A' || ch=='E' || ch=='I' || ch=='O' || ch=='U')
            {
                v++;
            }
            else if(ch>='a' && ch<='z' || ch>='A' && ch<='Z')
            {
                c++;
            }
        }
        System.out.println("Vowels are: " + v);
        System.out.println("Conconants are: " +c);
    }
}