def display_tasks(tasks):
    print("\nTo-Do List:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")

def add_task(tasks, task):
    tasks.append(task)
    print(f"Added task: {task}")

def remove_task(tasks, task_index):
    if 0 < task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number")

def main():
    tasks = []
    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter choice (1/2/3/4): ")

        if choice == '1':
            task = input("Enter task description: ")
            add_task(tasks, task)
        elif choice == '2':
            task_index = int(input("Enter task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == '3':
            display_tasks(tasks)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid input")

if __name__ == "__main__":
    main()
