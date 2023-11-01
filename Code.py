class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department, emp_experience):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department
        self.emp_experience = emp_experience

# Create a list to store employees
employee_list = []

# Function to add an employee to the system
def add_employee():
    emp_id = input("Enter Employee ID: ")
    emp_name = input("Enter Employee Name: ")
    emp_salary = float(input("Enter Base Salary: "))
    emp_department = input("Enter Employee Department: ")
    emp_experience = float(input("Enter Employee Experience (in years): "))
    
    # Calculate salary with an experience bonus
    experience_bonus = 1000 * emp_experience
    total_salary = emp_salary + experience_bonus
    
    employee = Employee(emp_id, emp_name, total_salary, emp_department, emp_experience)
    employee_list.append(employee)
    print(f"Employee {emp_name} added successfully.")

# Function to display all employees
def display_employees():
    for employee in employee_list:
        print(f"ID: {employee.emp_id}, Name: {employee.emp_name}, Salary: {employee.emp_salary}, Department: {employee.emp_department}, Experience: {employee.emp_experience} years")

# Function to update employee information
def update_employee(emp_id):
    for employee in employee_list:
        if employee.emp_id == emp_id:
            emp_name = input("Enter Updated Employee Name: ")
            emp_salary = float(input("Enter Updated Base Salary: "))
            emp_department = input("Enter Updated Employee Department: ")
            emp_experience = float(input("Enter Updated Employee Experience (in years): "))
            
            # Calculate salary with an experience bonus
            experience_bonus = 1000 * emp_experience
            total_salary = emp_salary + experience_bonus
            
            employee.emp_name = emp_name
            employee.emp_salary = total_salary
            employee.emp_department = emp_department
            employee.emp_experience = emp_experience
            print(f"Employee {employee.emp_name}'s information updated successfully.")
            return
    print(f"Employee with ID {emp_id} not found.")

# Function to delete an employee
def delete_employee(emp_id):
    for employee in employee_list:
        if employee.emp_id == emp_id:
            employee_list.remove(employee)
            print(f"Employee {employee.emp_name} deleted successfully.")
            return
    print(f"Employee with ID {emp_id} not found.")

# Main menu for the user interface
while True:
    print("\nEmployee Management System")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employees()
    elif choice == "3":
        emp_id = input("Enter Employee ID to update: ")
        update_employee(emp_id)
    elif choice == "4":
        emp_id = input("Enter Employee ID to delete: ")
        delete_employee(emp_id)
    elif choice == "5":
        print("Exiting Employee Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
