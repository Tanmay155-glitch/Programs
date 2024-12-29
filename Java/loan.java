public class loan
{
    public static void main(String args[])
    {
        String[] customerIds = {"C001", "C002", "C003", "C004", "C005"};

        String[] customerNames = {"John Doe", "Jane Smith", "Bob Johnson", "Alice Brown", "Mike Wilson"};

        double[] monthlyIncomes = {30000, 22000, 45000, 20000, 28000};

        System.out.println("Eligible Customers for Loan:");

        for (int i = 0; i < customerIds.length; i++) {
            if (monthlyIncomes[i] > 25000) {
                System.out.println("Customer ID: " + customerIds[i] + 
                                ", Name: " + customerNames[i] + 
                                ", Income: " + monthlyIncomes[i]);
            }
        }
    }
}