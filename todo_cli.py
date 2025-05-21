# A simple To-Do List CLI App with "Mark as Done" feature

# Each task is stored as a dictionary with keys: 'title' and 'done'
tasks = []

# Display the menu options to the user
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Mark task as done")
    print("4. Remove a task")
    print("5. Exit")

# Display all tasks, showing whether each is done or not
def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            # Display check mark if task is done, cross if not
            status = "✔" if task['done'] else "✖"
            print(f"{i}. [{status}] {task['title']}")

# Add a new task to the list, with 'done' initially set to False
def add_task():
    title = input("Enter a new task: ")
    tasks.append({'title': title, 'done': False})
    print(f"Task '{title}' added.")

# Mark a specific task as done by updating its 'done' status to True
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

# Remove a task by its number (1-based index)
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

# Main loop to keep the app running until user chooses to exit
def main():
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
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# This ensures the script runs only when executed directly
if __name__ == "__main__":
    main()
