import java.util.Scanner;

public class TwoDimensional_16 {
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.print("Enter the size of the array: ");
        int size = sc.nextInt();
        
        int[] array = new int[size];
        
        System.out.println("Enter elements of the array:");
        for (int i = 0; i < size; i++) {
            array[i] = sc.nextInt();
        }
        int choice=0;
        while(true)
        {
            System.out.println("\nSelect an operation:");
            System.out.println("1. Sum of array elements");
            System.out.println("2. Sort array in ascending order");
            System.out.println("3. Sort array in descending order");
            System.out.println("4. Find minimum element");
            System.out.println("5. Find maximum element");
            System.out.println("6. Calculate average of array elements");
            System.out.println("7.Exit");
            System.out.print("Enter your choice: ");
            choice = sc.nextInt();
            
            switch(choice) {
                case 1:
                    int sum = 0;
                    for (int i = 0; i < size; i++) {
                        sum += array[i];
                    }
                    System.out.println("Sum of array elements: " + sum);
                    break;
                    
                case 2:
                    for (int i = 0; i < size - 1; i++) {
                        for (int j = i + 1; j < size; j++) {
                            if (array[i] > array[j]) {
                                int temp = array[i];
                                array[i] = array[j];
                                array[j] = temp;
                            }
                        }
                    }
                    System.out.print("Array sorted in ascending order: ");
                    for (int i = 0; i < size; i++) {
                        System.out.print(array[i] + " ");
                    }
                    System.out.println();
                    break;
                    
                case 3:
                    for (int i = 0; i < size - 1; i++) {
                        for (int j = i + 1; j < size; j++) {
                            if (array[i] < array[j]) {
                                int temp = array[i];
                                array[i] = array[j];
                                array[j] = temp;
                            }
                        }
                    }
                    System.out.print("Array sorted in descending order: ");
                    for (int i = 0; i < size; i++) {
                        System.out.print(array[i] + " ");
                    }
                    System.out.println();
                    break;
                    
                case 4:
                    int min = array[0];
                    for (int i = 1; i < size; i++) {
                        if (array[i] < min) {
                            min = array[i];
                        }
                    }
                    System.out.println("Minimum element in the array: " + min);
                    break;
                    
                case 5:
                    int max = array[0];
                    for (int i = 1; i < size; i++) {
                        if (array[i] > max) {
                            max = array[i];
                        }
                    }
                    System.out.println("Maximum element in the array: " + max);
                    break;
                    
                case 6:
                    int total = 0;
                    for (int i = 0; i < size; i++) {
                        total += array[i];
                    }
                    double average = (double) total / size;
                    System.out.println("Average of array elements: " + average);
                    break;
                    
                case 7:
                    System.exit(0);
                    break;

                default:
                    System.out.println("Invalid choice");
            }
        }
    }
}