import os

TODO_FILE = "todo.txt"

def initialize_file():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w") as f:
            pass

def load_tasks():
    with open(TODO_FILE, "r") as f:
        tasks = [line.strip() for line in f.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("\n📭 No tasks found.\n")
    else:
        print("\n📝 Your To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
        print()

def add_task():
    task = input("Enter new task: ").strip()
    if task:
        tasks = load_tasks()
        tasks.append(task)
        save_tasks(tasks)
        print("✅ Task added successfully!\n")
    else:
        print("⚠️ Task cannot be empty.\n")

def delete_task():
    tasks = load_tasks()
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            save_tasks(tasks)
            print(f"🗑️ Task '{removed}' deleted.\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def main():
    initialize_file()
    while True:
        print("===== TO-DO LIST MENU =====")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            print("👋 Exiting... Have a productive day!")
            break
        else:
            print("⚠️ Invalid option. Please try again.\n")

if __name__ == "__main__":
    main()
