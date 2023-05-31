import json

class TaskManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1
        self.load_tasks_from_file()

    def load_tasks_from_file(self):
        try:
            with open('tasks.json', 'r', encoding='utf-8') as file:
                data = json.load(file)
                self.tasks = data['tasks']
                self.next_id = data['next_id']
        except FileNotFoundError:
            self.tasks = {}
            self.next_id = 1

    def save_tasks_to_file(self):
        data = {
            'tasks': self.tasks,
            'next_id': self.next_id
        }
        try:
            with open('tasks.json', 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4)
            print("Tasks saved to file successfully!")
        except Exception as e:
            print("An error occurred while saving tasks to file:", str(e))

    def add_task(self):
        try:
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            deadline = input("Enter task deadline: ")

            task = {
                'title': title,
                'description': description,
                'deadline': deadline,
                'description_shown': False  
            }
            self.tasks[self.next_id] = task
            self.next_id += 1
            self.save_tasks_to_file()
            print("Task added successfully!")
        except Exception as e:
            print("An error occurred while adding the task:", str(e))

    def display_task(self, task_id):
        task = self.tasks[task_id]
        print("ID:", task_id)
        print("Title:", task['title'])
        print("Deadline:", task['deadline'])
        if not task['description_shown']:  
            show_description = input("Show description? (y/n): ")
            if show_description.lower() == 'y':
                print("Description:", task['description'])
                task['description_shown'] = True  

    def view_tasks(self):
        try:
            if not self.tasks:
                print("No tasks found.")
            else:
                for task_id in self.tasks:
                    self.display_task(task_id)
                    print()
        except Exception as e:
            print("An error occurred while viewing tasks:", str(e))

    def delete_task(self):
        try:
            task_id = int(input("Enter the ID of the task to delete: "))
            if task_id in self.tasks:
                del self.tasks[task_id]
                self.save_tasks_to_file()
                print("Task deleted successfully!")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid task ID. Please enter a valid number.")
        except Exception as e:
            print("An error occurred while deleting the task:", str(e))

    def update_task(self):
        try:
            task_id = int(input("Enter the ID of the task to update: "))
            if task_id in self.tasks:
                task = self.tasks[task_id]
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
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid task ID. Please enter a valid number.")
        except Exception as e:
            print("An error occurred while updating the task:", str(e))

    def manual_save_to_file(self):
        try:
            self.save_tasks_to_file()
        except Exception as e:
            print("An error occurred while manually saving tasks to file:", str(e))

    def run(self):
        try:
            self.view_tasks() 

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
        except Exception as e:
            print("An error occurred while running the task manager:", str(e))


if __name__ == '__main__':
    task_manager = TaskManager()
    task_manager.run()
