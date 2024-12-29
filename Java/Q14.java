//Write a Java program to reverse the array
public class Q14 {
    public static void main(String[] args) {
        int[] array = {1, 2, 3, 4, 5};
        
        // Reverse the array
        for (int i = 0; i < array.length / 2; i++) {
            int temp = array[i];
            array[i] = array[array.length - 1 - i];
            array[array.length - 1 - i] = temp;
        }
        
        // Print the reversed array
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}
