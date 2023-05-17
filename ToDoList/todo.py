import json

class TaskManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks_from_file()

    def load_tasks_from_file(self):
        try:
            with open('tasks.json', 'r') as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks_to_file(self):
        with open('tasks.json', 'w') as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self):
        title = input("Enter task title: ")
        description = input("Enter task description: ")
        deadline = input("Enter task deadline: ")

        task = {
            'id': len(self.tasks) + 1,
            'title': title,
            'description': description,
            'deadline': deadline
        }
        self.tasks.append(task)
        self.save_tasks_to_file()
        print("Task added successfully!")

    def display_task(self, task):
        print("ID:", task['id'])
        print("Title:", task['title'])
        print("Deadline:", task['deadline'])
        show_description = input("Show description? (y/n): ")
        if show_description.lower() == 'y':
            print("Description:", task['description'])

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for task in self.tasks:
                self.display_task(task)
                print()

    def delete_task(self):
        task_id = int(input("Enter the ID of the task to delete: "))
        for task in self.tasks:
            if task['id'] == task_id:
                self.tasks.remove(task)
                self.save_tasks_to_file()
                print("Task deleted successfully!")
                return
        print("Task not found.")

    def update_task(self):
        task_id = int(input("Enter the ID of the task to update: "))
        for task in self.tasks:
            if task['id'] == task_id:
                print("Enter new task details (leave empty to keep the existing value):")
                title = input("Enter task title: ")
                description = input("Enter task description: ")
                deadline = input("Enter task deadline: ")

                if title:
                    task['title'] = title
                if description:
                    task['description'] = description
                if deadline:
                    task['deadline'] = deadline

                self.save_tasks_to_file()
                print("Task updated successfully!")
                return
        print("Task not found.")

    def manual_save_to_file(self):
        self.save_tasks_to_file()
        print("Tasks saved to file successfully!")

    def run(self):
        while True:
            print("\nTask Manager")
            print("1. Add Task")
            print("2. View Tasks")
            print("3. Delete Task")
            print("4. Update Task")
            print("5. Manual Save to File")
            print("6. Exit")

            choice = input("Enter your choice (1-6): ")
            print()

            if choice == '1':
                self.add_task()
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.delete_task()
            elif choice == '4':
                self.update_task()
            elif choice == '5':
                self.manual_save_to_file()
            elif choice == '6':
                self.save_tasks_to_file()
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.run()
