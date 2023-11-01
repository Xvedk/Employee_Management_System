# Employee_Management_System
Employee Management System in Python involves several components, including data storage, user interface, and functionality for managing employees. 
The provided Python code represents an Employee Management System, facilitating the management of employee records. It employs an `Employee` class to encapsulate essential employee details, including their ID, name, base salary, department, and experience in years. The system maintains a list, `employee_list`, to store instances of the `Employee` class.

The code offers several functions to manage employees:

1. `add_employee()`: This function collects user input for an employee's information, computes their total salary by adding a $1000 bonus for each year of experience, and creates an `Employee` object that is then appended to the `employee_list`.

2. `display_employees()`: It iterates through the `employee_list`, displaying the details of each employee, including their calculated total salary based on experience.

3. `update_employee(emp_id)`: This function allows users to modify employee details by providing their ID. Users can update the name, base salary, department, and experience, and the code recalculates the total salary accordingly.

4. `delete_employee(emp_id)`: Users can remove an employee record by specifying the employee's ID.

The main menu is structured as a loop, presenting users with options to interact with the system, including adding, displaying, updating, and deleting employee records, and the ability to exit the program. This code serves as a fundamental Employee Management System with an integrated salary calculation based on experience. Further enhancements may include error handling, data persistence mechanisms, or a more user-friendly interface.
