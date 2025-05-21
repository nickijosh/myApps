import json
import os

# Filename to store tasks persistently
FILENAME = "tasks.json"

# Tasks will be loaded into this list at startup
tasks = []

# Load tasks from file if it exists
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            try:
                data = json.load(f)
                # Only load valid task dictionaries
                if isinstance(data, list):
                    global tasks
                    tasks = data
            except json.JSONDecodeError:
                print("Warning: Could not parse tasks file. Starting fresh.")

# Save current tasks to file
def save_tasks():
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)

# Display menu options
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as done")
    print("4. Remove a task")
    print("5. Exit")

# Show tasks with status symbols
def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "✔" if task.get('done') else "✖"
            print(f"{i}. [{status}] {task.get('title')}")

# Add a new task to the list
def add_task():
    title = input("Enter a new task: ")
    tasks.append({'title': title, 'done': False})
    print(f"Task '{title}' added.")

# Mark a task as done
def mark_task_done():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to mark as done: "))
            if 1 <= task_num <= len(tasks):
                tasks[task_num - 1]['done'] = True
                print("Task marked as done.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Remove a task from the list
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Task '{removed['title']}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main app loop
def main():
    load_tasks()  # Load tasks at the start

    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            save_tasks()  # Save tasks before exiting
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
