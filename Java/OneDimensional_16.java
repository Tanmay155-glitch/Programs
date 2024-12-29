import java.util.Scanner;
public class OneDimensional_16 {
    
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of rows: ");
        int rows = sc.nextInt();
        System.out.print("Enter the number of columns: ");
        int cols = sc.nextInt();
        
        int[][] matrix1 = new int[rows][cols];
        int[][] matrix2 = new int[rows][cols];
        int[][] result = new int[rows][cols];
        
        System.out.println("Enter elements of the first matrix:");
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < cols; j++) 
            {
                matrix1[i][j] = sc.nextInt();
            }
        }
        
        System.out.println("Enter elements of the second matrix:");
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < cols; j++) 
            {
                matrix2[i][j] = sc.nextInt();
            }
        }
        
        System.out.println("\nAddition of two matrices:");
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < cols; j++) 
            {
                result[i][j] = matrix1[i][j] + matrix2[i][j];
            }
        }
        for (int i = 0; i < result.length; i++) 
        {
            for (int j = 0; j < result[i].length; j++) 
            {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
        
        System.out.println("\nSubtraction of two matrices:");
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < cols; j++) 
            {
                result[i][j] = matrix1[i][j] - matrix2[i][j];
            }
        }
        for (int i = 0; i < result.length; i++) 
        {
            for (int j = 0; j < result[i].length; j++) 
            {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
        
        System.out.println("\nMultiplication of two matrices:");
        if (cols == rows) 
        {  
            for (int i = 0; i < rows; i++) 
            {
                for (int j = 0; j < cols; j++) 
                {
                    result[i][j] = 0;
                    for (int k = 0; k < cols; k++) 
                    {
                        result[i][j] += matrix1[i][k] * matrix2[k][j];
                    }
                }
            }
            for (int i = 0; i < result.length; i++) 
            {
                for (int j = 0; j < result[i].length; j++) 
                {
                    System.out.print(result[i][j] + " ");
                }
                System.out.println();
            }
        } 

        
        System.out.println("\nDivision of two matrices :");
        for (int i = 0; i < rows; i++) 
        {
            for (int j = 0; j < cols; j++) 
            {
                if (matrix2[i][j] != 0) 
                {
                    result[i][j] = matrix1[i][j] / matrix2[i][j];
                } 
                else 
                {
                    result[i][j] = 0;
                }
            }
        }
        for (int i = 0; i < result.length; i++) 
        {
            for (int j = 0; j < result[i].length; j++) 
            {
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}