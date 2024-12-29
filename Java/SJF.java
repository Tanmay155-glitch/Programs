import java.util.*;

class SJF {
    // Function to find the waiting time for all processes
    static void findWaitingTime(int processes[], int n, int bt[], int wt[]) {
        // Waiting time for the first process is 0
        wt[0] = 0;

        // Calculating waiting time for each process
        for (int i = 1; i < n; i++) {
            wt[i] = bt[i - 1] + wt[i - 1];
        }
    }

    // Function to calculate turn around time
    static void findTurnAroundTime(int processes[], int n, int bt[], int wt[], int tat[]) {
        // Calculating turn around time by adding burst time and waiting time
        for (int i = 0; i < n; i++) {
            tat[i] = bt[i] + wt[i];
        }
    }

    // Function to calculate average waiting and turn-around times and display Gantt chart
    static void findAvgTime(int processes[], int n, int bt[]) {
        int wt[] = new int[n]; // Waiting times
        int tat[] = new int[n]; // Turn-around times
        int completionTime[] = new int[n]; // Completion times

        // Find waiting time of all processes
        findWaitingTime(processes, n, bt, wt);

        // Find turn around time for all processes
        findTurnAroundTime(processes, n, bt, wt, tat);

        // Display processes with their burst time, waiting time, and turn-around time
        System.out.println("Processes  Burst Time  Waiting Time  Turn-Around Time  Completion Time");

        int total_wt = 0, total_tat = 0;
        for (int i = 0; i < n; i++) {
            total_wt += wt[i];
            total_tat += tat[i];
            completionTime[i] = tat[i]; // Completion time is equal to turn-around time
            System.out.println("   " + processes[i] + "\t\t" + bt[i] + "\t\t" + wt[i] + "\t\t" + tat[i] + "\t\t" + completionTime[i]);
        }

        // Calculate and display average waiting and turn-around time
        System.out.println("\nAverage Waiting Time = " + (float) total_wt / n);
        System.out.println("Average Turn-Around Time = " + (float) total_tat / n);

        // Display Gantt chart
        displayGanttChart(processes, n, bt, wt);
    }

    // Function to display the Gantt chart
    static void displayGanttChart(int processes[], int n, int bt[], int wt[]) {
        System.out.println("\nGantt Chart:");
        
        // Print process numbers
        for (int i = 0; i < n; i++) {
            System.out.print("|  P" + processes[i] + "  ");
        }
        System.out.println("|");

        // Print start times for each process
        for (int i = 0; i < n; i++) {
            System.out.print(wt[i] + "\t");
        }
        // Print the last completion time
        System.out.print(wt[n-1] + bt[n-1]);
        System.out.println();
    }

    // Driver code
    public static void main(String[] args) {
        int processes[] = {1, 2, 3, 4};  // Process IDs
        int n = processes.length;        // Number of processes

        // Burst time of all processes
        int burst_time[] = {6, 8, 7, 3};

        // Sort processes by burst time (Shortest Job First)
        int sortedProcesses[] = new int[n];
        int sortedBurstTime[] = new int[n];
        for (int i = 0; i < n; i++) {
            sortedProcesses[i] = processes[i];
            sortedBurstTime[i] = burst_time[i];
        }

        // Sorting burst time in ascending order
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (sortedBurstTime[i] > sortedBurstTime[j]) {
                    // Swap burst times
                    int temp = sortedBurstTime[i];
                    sortedBurstTime[i] = sortedBurstTime[j];
                    sortedBurstTime[j] = temp;

                    // Swap process IDs
                    int tempProcess = sortedProcesses[i];
                    sortedProcesses[i] = sortedProcesses[j];
                    sortedProcesses[j] = tempProcess;
                }
            }
        }

        // Find average time and display Gantt chart
        findAvgTime(sortedProcesses, n, sortedBurstTime);
    }
}
