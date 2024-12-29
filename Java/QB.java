import java.util.*; 
class QB {
public static void main(String[] args) {
Scanner s = new Scanner(System.in); 
System.out.println("Enter First Number:"); 
int first = s.nextInt();
System.out.println("Enter Second Number:"); 
int second = s.nextInt();
int And = first & second; 
int Or = first | second; 
int Xor = first ^ second;
System.out.println("Bitwise AND: " + And);
System.out.println("Bitwise OR: " + Or);
System.out.println("Bitwise XOR: " + Xor); 
    }
}