class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary

    def __str__(self):
        return f"{self.employee_id}, {self.name}, {self.position}, {self.salary}\n"
    
class EmployeeManager:
    def __init__(self):
        self.filename = "employees.txt"
    
    def add_employee(self):
        try:
            with open(self.filename, mode='r') as file:
                employee_id = input("Enter Employee ID: ")
                unique = False
                while not unique:
                    unique = True
                    for line in file:
                        if line.startswith(employee_id + ','):
                            employee_id = input("Employee ID already exists. Please enter another ID: ")
                            unique = False
                            break
                name = input("Enter Name: ")
                position = input("Enter Position: ")
                salary = int(input("Enter Salary: "))
                emp = Employee(employee_id, name, position, salary)
            with open(self.filename, mode='a') as file:
                file.write(str(emp))
            print("Employee added successfully!")
        except FileNotFoundError:
            print("File Not Found!")


    def view_all(self):
        try:
            with open(self.filename, mode='r') as file:
                if not file.readlines():
                    print("No recordes found.")
                    return
                file.seek(0)
                print("Employee Records:")
                for line in file.readlines():
                    print(line.strip())
        except FileNotFoundError:
            print("File Not Found!")

    def search(self):
        employee_id = input("Enter Employee ID to search: ")
        try:
            with open(self.filename) as file:
                for line in file:
                    if line.startswith(employee_id + ','):
                        print("Employee Found:")
                        print(line.strip())
                        return
                print("Employee Not Found!")
        except FileNotFoundError:
            print("File Not Found!")
    
    def update(self, employee_found = False):
        employee_id = input("Enter Employee ID to update: ")
        try:
            lines = []
            with open(self.filename, mode='r') as file:
                for line in file:
                    lines.append(line)
            with open(self.filename, mode='w') as file:
                for line in lines:
                    if line.startswith(employee_id + ','):
                        print("Employee Found:")
                        employee_found = True
                        employee_id = input("Enter updated Employee ID: ")
                        name = input("Enter updated Name: ")
                        position = input("Enter updated Position: ")
                        salary = int(input("Enter updated Salary: "))
                        emp = Employee(employee_id, name, position, salary)
                        file.write(str(emp))
                        print("Employee updated successfully!")
                    else:
                        file.write(line)
                if not employee_found:
                    print("Employee Not Found!")
        except FileNotFoundError:
            print("File Not Found!")

    def delete(self, employee_found = False):
        employee_id = input("Enter Employee ID to delete: ")
        try:
            lines = []
            with open(self.filename, mode='r') as file:
                for line in file:
                    lines.append(line)
            with open(self.filename, mode='w') as file:
                for line in lines:
                    if line.startswith(employee_id + ','):
                        print("Employee Deleted!")
                        employee_found = True
                    else:
                        file.write(line)
                if not employee_found:
                    print("Employee Not Found!")
        except FileNotFoundError:
            print("File Not Found!")

    def sort_employee(self, by = "name"):
        try:
            with open(self.filename, mode='r') as file:
                lines = [line.strip().split(', ') for line in file]

            if by == 'name':
                lines.sort(key=lambda x: x[1])
            elif by == 'position':
                lines.sort(key=lambda x: x[2])
            elif by == 'salary':
                lines.sort(key=lambda x: int(x[3]), reverse = True)
            
            
            print("Employee Records:")
            print(f"Sorted by {by}:")
            for line in lines:
                print(', '.join(line))
        except FileNotFoundError:
            print("File Not Found!")

    def exit(self):
        print("Goodbye!")

    def menu(self):
        print("""Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")
        while True:
            num = int(input("\nEnter your choice: "))
            if num == 1:
                self.add_employee()
            elif num == 2:
                self.sort_employee('salary')
            elif num == 3:
                self.search()
            elif num == 4:
                self.update()
            elif num == 5:
                self.delete()
            elif num == 6:
                self.exit()
                break
            else:
                print("Invalid input!")

manager = EmployeeManager()
manager.menu()