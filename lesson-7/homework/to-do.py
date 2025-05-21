class ToDoList:
    def __init__(self, filename = "tasks.txt"):
        self.filename = filename
        self.tasks = self.load_tasks()
    
    def load_tasks(self):
        tasks = []
        try:
            with open(self.filename, 'r') as file:
                for line in file:
                    task = list(line.strip().split(', '))
                    if task:
                        tasks.append(task)
            print("Tasks loaded successfully!")
        except FileNotFoundError:
            print("File not found!")
        return tasks
    
    def save_tasks(self):
        with open(self.filename, 'w') as file:
            for line in self.tasks:
                file.write(f'{(line[0])}, {line[1]}, {line[2]}, {line[3]}, {line[4]}\n')
        print("Tasks saved successfully!")

    def add_task(self):
                task_id = input("Enter Task ID: ")
                unique = False
                while not unique:
                    unique = True
                    for line in self.tasks:
                        if line[0] == task_id:
                            task_id = input("Task ID already exists. Please enter another ID: ")
                            unique = False
                            break
                title = input("Enter Title: ")
                description = input("Enter Description: ")
                due_date = input("Enter Due Date (YYYY-MM-DD): ")
                status = input("Enter Status (Pending/In Progress/Completed): ")
                self.tasks.append([task_id, title, description, due_date, status])
                print("Task added successfully!")


    def view_all(self):
                if not len(self.tasks):
                    print("No recordes found.")
                    return
                print("Tasks:")
                for line in self.tasks:
                    print(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}')
    
    def update(self, task_found = False):
                task_id = input("Enter Task ID to update: ")
                for line in self.tasks:
                    if line[0] == task_id:
                        print("Task Found:")
                        task_found = True
                        line[1] = input("Enter updated Title: ")
                        line[2] = input("Enter updated Description: ")
                        line[3] = input("Enter updated Due Date (YYYY-MM-DD): ")
                        line[4] = input("Enter updated Status (Pending/In Progress/Completed): ")
                        print("Task updated successfully!")
                        break
                if not task_found:
                    print("Task Not Found!")

    def delete(self, task_found = False):
                task_id = input("Enter Employee ID to update: ")
                for line in self.tasks:
                    if line[0] == task_id:
                        print("Task Deleted!")
                        self.tasks.remove(line)
                        task_found = True
                if not task_found:
                    print("Task Not Found!")

    def filter(self, by = "Pending"):
        print(f"Filtered by {by}")
        for line in self.tasks:
            if line[4] == by:
                print(f'{line[0]}, {line[1]}, {line[2]}, {line[3]}, {line[4]}')

    def exit(self):
        print("Goodbye!")

    def menu(self):
        print("""Welcome to the To-Do Application!
1. Add a new task
2. View all tasks
3. Update a task
4. Delete a task
5. Filter tasks by status
6. Save tasks
7. Load tasks
8. Exit""")
        while True:
            num = int(input("\nEnter your choice: "))
            if num == 1:
                self.add_task()
            elif num == 2:
                self.view_all()
            elif num == 3:
                self.update()
            elif num == 4:
                self.delete()
            elif num == 5:
                self.filter()
            elif num == 6:
                self.save_tasks()
            elif num == 7:
                self.load_tasks()
            elif num == 8:
                self.exit()
                break
            else:
                print("Invalid input!")

List = ToDoList()
List.menu()