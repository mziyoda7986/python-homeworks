def add_employee():
    with open("employee.txt", 'a') as file:
        employee_data = input("Enter an employee's datas: ")
        file.write(employee_data + '\n')
        print("Employee added!")

def display():
    try:
        with open("employee.txt", 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("File not found!")

def search():
    try:
        eid = input("Enter an employee ID: ")
        b = True
        with open("employee.txt", 'r') as file:
            for line in file:
                if line.startswith(eid + ','):
                    print("Employee found!")
                    print(line)
                    b = False
                    break
            if b:
                print("Employee Not found!") 
    except FileNotFoundError:
        print("File not found!")

def update():
    try:
        eid = input("Enter an employee ID: ")
        b = True
        lines = []
        with open("employee.txt", 'r') as file:
            lines = file.readlines()
        with open("employee.txt", 'w') as file:
            for line in lines:
                if line.startswith(eid + ',') and b:
                    employee_data = input("Enter an employee's datas: ")
                    file.write(employee_data)
                    print("Employee updated!")
                    b = False
                else:
                    file.write(line)
            if b:
                print("Employee Not found!") 
    except FileNotFoundError:
        print("File not found!")

def delete_employee():
    try:
        eid = input("Enter an employee ID: ")
        b = True
        lines = []
        with open("employee.txt", 'r') as file:
            lines = file.readlines()
        with open("employee.txt", 'w') as file:
            for line in lines:
                if line.startswith(eid + ',') and b:
                    print("Employee deleted!")
                    b = False
                else:
                    file.write(line)
            if b:
                print("Employee Not found!") 
    except FileNotFoundError:
        print("File not found!")



try:
    a = int(input("""1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit
      
Chose one option(with number): """))
    
    if a == 1 :
        add_employee()
    elif a == 2:
        display()
    elif a == 3:
        search()
    elif a == 4:
        update()
    elif a == 5:
        delete_employee()
    elif a == 6:
        print("Exit")
    else:
        print("Invalid choise!")
except ValueError:
    print("Incorrect value!")