import json

todo_list = []
while True:
    task = input("Enter a new task (or 'exit' to quit): ")
    if task.lower() == 'exit':
        break
    todo_list.append(task)

with open('todo.json', 'w') as file:
    json.dump(todo_list, file)

print("Todo list saved to 'todo.json'")
