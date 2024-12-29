from collections import deque

# Initial setup for processes
processes = [
    {'pid': 1, 'burst_time': 5, 'remaining_time': 10, 'completion_time': 0},
    {'pid': 2, 'burst_time': 4, 'remaining_time': 5, 'completion_time': 0},
    {'pid': 3, 'burst_time': 2, 'remaining_time': 8, 'completion_time': 0},
    {'pid': 4, 'burst_time': 1, 'remaining_time': 5, 'completion_time': 0},
]
quantum = 2
time = 0
gantt_chart = []

# Convert processes list into a deque for efficient popping from the front
ready_queue = deque(processes)

# Round Robin Scheduling
while ready_queue:
    process = ready_queue.popleft()  # Get the first process in the queue
    if process['remaining_time'] > quantum:
        gantt_chart.append((process['pid'], time, time + quantum))
        time += quantum
        process['remaining_time'] -= quantum
        ready_queue.append(process)  # Re-add the process to the queue if it has remaining time
    else:
        gantt_chart.append((process['pid'], time, time + process['remaining_time']))
        time += process['remaining_time']
        process['remaining_time'] = 0
        process['completion_time'] = time  # Set completion time

# Output the Gantt chart
print("\nGantt Chart:")
for entry in gantt_chart:
    print(f"Process {entry[0]}: [{entry[1]} - {entry[2]}]")

# Output the process completion times
print("\nProcess Completion Times:")
for process in processes:
    print(f"Process {process['pid']}: Completion Time = {process['completion_time']}")
