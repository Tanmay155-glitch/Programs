import matplotlib.pyplot as plt

processes = ['P1', 'P2', 'P3', 'P4']
arrival_time = [0, 1, 5, 6]
burst_time = [2, 2, 3, 4]


start_time = [0] * len(processes)
completion_time = [0] * len(processes)

start_time[0] = arrival_time[0]
completion_time[0] = start_time[0] + burst_time[0]

for i in range(1, len(processes)):
    start_time[i] = max(completion_time[i - 1], arrival_time[i])  
    completion_time[i] = start_time[i] + burst_time[i]

turnaround_time = [0] * len(processes)
waiting_time = [0] * len(processes)

for i in range(len(processes)):
    turnaround_time[i] = completion_time[i] - arrival_time[i]
    waiting_time[i] = turnaround_time[i] - burst_time[i]

process_table = list(zip(processes, arrival_time, burst_time, start_time, completion_time, turnaround_time, waiting_time))

fig, gnt = plt.subplots(figsize=(10, 4))

gnt.set_ylim(0, 50)
gnt.set_xlim(0, completion_time[-1])
gnt.set_xlabel('Time')
gnt.set_ylabel('Processes')

gnt.set_yticks([15])
gnt.set_yticklabels(['Processes'])

for i in range(len(processes)):
    gnt.broken_barh([(start_time[i], burst_time[i])], (10, 10), facecolors=('tab:blue'))
    gnt.text(start_time[i] + burst_time[i] / 2 - 0.25, 15, processes[i], fontsize=10, color='white', fontweight='bold')

plt.title("Gantt Chart for FCFS Scheduling")
plt.grid(True)
plt.show()

process_table  
