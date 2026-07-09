# Exercise 4: Employee Management System

## 1. Understand Array Representation
The employee records are stored in a list, which acts as an array in Python. Each employee is represented as a dictionary containing the employee ID, name, department, and salary.

## 2. Setup
Run the program using:

```bash
python employee_management.py
```

## 3. Implementation
The script supports these operations:
- Display all employees
- Add a new employee
- Search for an employee by ID
- Update employee details
- Remove an employee
- Calculate average salary

## 4. Analysis
- Adding an employee takes $O(1)$ time on average because it appends to the end of the list.
- Searching, updating, and removing an employee take $O(n)$ time because the program may scan the array linearly.
- The solution is simple and easy to understand while still demonstrating effective array-based record management.
