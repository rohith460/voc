import json

# Define a class to represent a task.
class Task:
    def __init__(self, title, description, category, completed=False):
        self.title = title
        self.description = description
        self.category = category
        self.completed = completed  # Mark task as completed or not

    def mark_completed(self):
        self.completed = True

# Function to save the current list of tasks to a JSON file.
def save_tasks(tasks):
    with open('tasks.json', 'w') as f:
        json.dump([task.__dict__ for task in tasks], f, indent=4)

# Function to load tasks from the JSON file.
def load_tasks():
    try:
        with open('tasks.json', 'r') as f:
            tasks_data = json.load(f)
            return [Task(data['title'], data['description'], data['category'], data.get('completed', False)) for data in tasks_data]
    except FileNotFoundError:
        return []  # If the file doesn't exist, return an empty list

# Main function to run the application and display the menu.
def main():
    tasks = load_tasks()  # Load tasks from file on startup

    while True:
        print("\n+-+-+ Personal To-Do List +-+-+")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task Completed")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_task(tasks)  # Add a new task
        elif choice == '2':
            view_tasks(tasks)  # View all tasks
        elif choice == '3':
            mark_task_completed(tasks)  # Mark a task as completed
        elif choice == '4':
            delete_task(tasks)  # Delete a task
        elif choice == '5':
            save_tasks(tasks)  # Save tasks before exiting
            print("Goodbye! Your tasks have been saved.")
            break
        else:
            print("Invalid option, please enter a number between 1 and 5.")

# Function to add a new task to the list.
def add_task(tasks):
    print("\n!!! Add New Task !!!")
    title = input("Task title: ")
    description = input("Task description: ")
    category = input("Task category (e.g., Work, Personal, Urgent): ")
    task = Task(title, description, category)  # Create a new Task object
    tasks.append(task)
    print(f"Task '{title}' added successfully!\n")

# Function to display all tasks with their details and status.
def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks available.\n")
        return
    print("\n^^^^Task List^^^^^")
    for i, task in enumerate(tasks, start=1):
        status = "Completed" if task.completed else "Incomplete"
        print(f"{i}. {task.title} - {task.category} [{status}]\n    {task.description}")

# Function to mark a selected task as completed.
def mark_task_completed(tasks):
    if not tasks:
        print("\nNo tasks to complete.\n")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to mark as completed: ")) - 1
        if 0 <= task_num < len(tasks):
            tasks[task_num].mark_completed()
            print(f"Task '{tasks[task_num].title}' marked as completed.\n")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task from the list.
def delete_task(tasks):
    if not tasks:
        print("\nNo tasks to delete.\n")
        return
    view_tasks(tasks)
    try:
        task_num = int(input("\nEnter the task number to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted_task = tasks.pop(task_num)
            print(f"Task '{deleted_task.title}' deleted.\n")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
