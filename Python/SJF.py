# Function to find the waiting time for all processes
def find_waiting_time(processes, n, bt, wt):
    # Waiting time for first process is 0
    wt[0] = 0
  
    # Calculating waiting time for each process
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]
  
# Function to calculate turn around time
def find_turn_around_time(processes, n, bt, wt, tat):
    # Calculating turn around time by adding burst time and waiting time
    for i in range(n):
        tat[i] = bt[i] + wt[i]
  
# Function to calculate average waiting and turn-around times
def find_avg_time(processes, n, bt):
    wt = [0] * n  # Waiting times
    tat = [0] * n  # Turn-around times
  
    # Function to find waiting time of all processes
    find_waiting_time(processes, n, bt, wt)
  
    # Function to find turn around time for all processes
    find_turn_around_time(processes, n, bt, wt, tat)
  
    print("Processes Burst Time  Waiting Time  Turn-Around Time")
    total_wt = 0
    total_tat = 0
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        print(f" {i+1} \t\t {bt[i]} \t\t {wt[i]} \t\t {tat[i]}")
  
    print(f"\nAverage Waiting Time = {total_wt / n}")
    print(f"Average Turn-Around Time = {total_tat / n}")
  
# Driver code
if __name__ == "__main__":
    # Number of processes
    processes = [1, 2, 3, 4]
    n = len(processes)
  
    # Burst time of all processes
    burst_time = [6, 8, 7, 3]
  
    # Sorting processes by burst time (Shortest Job First)
    processes = [x for _, x in sorted(zip(burst_time, processes))]
    burst_time.sort()
  
    # Find average time
    find_avg_time(processes, n, burst_time)
