# todo_cli.py

# A list to store our tasks
tasks = []

# This function displays the menu options to the user
def show_menu():
    print("\nTo-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Remove a task")
    print("4. Exit")

# This function displays all current tasks
def view_tasks():
    if not tasks:
        print("No tasks yet.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):  # Enumerate starts counting from 1
            print(f"{i}. {task}")

# This function adds a new task to the list
def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

# This function removes a task based on its number in the list
def remove_task():
    view_tasks()
    if tasks:
        try:
            task_num = int(input("Enter task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)  # Remove task at the given index
                print(f"Task '{removed}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# This is the main loop of the program — it keeps the app running
def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            remove_task()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# This line ensures that the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()
