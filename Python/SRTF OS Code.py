class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.completion_time = 0
        self.turnaround_time = 0
        self.waiting_time = 0

def srtf_scheduling(processes):
    n = len(processes)
    time = 0
    completed_processes = 0
    gantt_chart = []

    while completed_processes < n:
        # Find the process with the shortest remaining time
        shortest_process_index = -1
        shortest_remaining_time = float('inf')
        
        for i in range(n):
            if (processes[i].arrival_time <= time and
                    processes[i].remaining_time < shortest_remaining_time and
                    processes[i].remaining_time > 0):
                shortest_remaining_time = processes[i].remaining_time
                shortest_process_index = i
        
        if shortest_process_index != -1:
            # Execute the selected process for 1 time unit
            processes[shortest_process_index].remaining_time -= 1
            gantt_chart.append(processes[shortest_process_index].pid)
            time += 1
            
            # If the process is completed
            if processes[shortest_process_index].remaining_time == 0:
                processes[shortest_process_index].completion_time = time
                processes[shortest_process_index].turnaround_time = (time - processes[shortest_process_index].arrival_time)
                processes[shortest_process_index].waiting_time = (processes[shortest_process_index].turnaround_time - processes[shortest_process_index].burst_time)
                completed_processes += 1
        else:
            # If no process is ready to execute, increment time
            gantt_chart.append("Idle")
            time += 1

    return gantt_chart

def print_processes(processes):
    print("PID\tArrival Time\tBurst Time\tCompletion Time\tTurnaround Time\tWaiting Time")
    for process in processes:
        print(f"{process.pid}\t{process.arrival_time}\t\t{process.burst_time}\t\t{process.completion_time}\t\t{process.turnaround_time}\t\t{process.waiting_time}")

def print_gantt_chart(gantt_chart):
    print("Gantt Chart:")
    print(" | ".join(map(str, gantt_chart)))

# Example usage
if __name__ == "__main__":
    processes = [
        Process(1, 0, 8),
        Process(2, 1, 4),
        Process(3, 2, 9),
        Process(4, 3, 5)
    ]

    gantt_chart = srtf_scheduling(processes)
    print_processes(processes)
    print_gantt_chart(gantt_chart)
