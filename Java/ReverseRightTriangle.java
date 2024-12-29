public class ReverseRightTriangle {
    public static void main(String[] args) {
        int n = 5; // Number of rows
        
        for (int i = n; i >= 1; i--) {
            // Print leading spaces
            for (int j = n - i; j > 0; j--) {
                System.out.print(" ");
            }
            // Print stars
            for (int k = 1; k <= i; k++) {
                System.out.print("*");
            }
            // Move to the next line
            System.out.println();
        }
    }
}
