from typing import List, Dict, Optional


Employee = Dict[str, object]


def display_employees(employees: List[Employee]) -> None:
    """Show all employee records stored in the array/list."""
    if not employees:
        print("No employees found.")
        return

    print("\nEmployee Records")
    print("-" * 60)
    for employee in employees:
        print(
            f"ID: {employee['employee_id']} | Name: {employee['name']} | "
            f"Department: {employee['department']} | Salary: ${employee['salary']:.2f}"
        )


def add_employee(employees: List[Employee], employee_id: int, name: str, department: str, salary: float) -> None:
    """Append a new employee record to the array."""
    employees.append(
        {
            "employee_id": employee_id,
            "name": name,
            "department": department,
            "salary": salary,
        }
    )
    print(f"Employee {name} added successfully.")


def search_employee(employees: List[Employee], employee_id: int) -> Optional[Employee]:
    """Find an employee using a linear search over the array."""
    for employee in employees:
        if employee["employee_id"] == employee_id:
            return employee
    return None


def update_employee(
    employees: List[Employee], employee_id: int, name: Optional[str] = None,
    department: Optional[str] = None, salary: Optional[float] = None
) -> bool:
    """Update an employee record in place."""
    for employee in employees:
        if employee["employee_id"] == employee_id:
            if name is not None:
                employee["name"] = name
            if department is not None:
                employee["department"] = department
            if salary is not None:
                employee["salary"] = salary
            return True
    return False


def remove_employee(employees: List[Employee], employee_id: int) -> bool:
    """Remove an employee record from the array."""
    for index, employee in enumerate(employees):
        if employee["employee_id"] == employee_id:
            employees.pop(index)
            return True
    return False


def average_salary(employees: List[Employee]) -> float:
    """Calculate the average salary for all employees."""
    if not employees:
        return 0.0
    return sum(float(employee["salary"]) for employee in employees) / len(employees)


def main() -> None:
    employees: List[Employee] = [
        {"employee_id": 101, "name": "Alice", "department": "HR", "salary": 50000},
        {"employee_id": 102, "name": "Bob", "department": "Engineering", "salary": 70000},
        {"employee_id": 103, "name": "Charlie", "department": "Finance", "salary": 65000},
    ]

    print("Employee Management System")
    print("=========================")

    while True:
        print("\n1. Display employees")
        print("2. Add employee")
        print("3. Search employee")
        print("4. Update employee")
        print("5. Remove employee")
        print("6. Show average salary")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_employees(employees)
        elif choice == "2":
            employee_id = int(input("Employee ID: "))
            name = input("Name: ")
            department = input("Department: ")
            salary = float(input("Salary: "))
            add_employee(employees, employee_id, name, department, salary)
        elif choice == "3":
            employee_id = int(input("Employee ID to search: "))
            result = search_employee(employees, employee_id)
            if result:
                print(f"Found: {result['name']} in {result['department']}")
            else:
                print("Employee not found.")
        elif choice == "4":
            employee_id = int(input("Employee ID to update: "))
            name = input("New name (leave blank to keep): ") or None
            department = input("New department (leave blank to keep): ") or None
            salary_input = input("New salary (leave blank to keep): ")
            salary = float(salary_input) if salary_input else None
            if update_employee(employees, employee_id, name, department, salary):
                print("Employee updated successfully.")
            else:
                print("Employee not found.")
        elif choice == "5":
            employee_id = int(input("Employee ID to remove: "))
            if remove_employee(employees, employee_id):
                print("Employee removed successfully.")
            else:
                print("Employee not found.")
        elif choice == "6":
            print(f"Average salary: ${average_salary(employees):.2f}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
