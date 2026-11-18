from langchain.tools import tool

# Employee data
employees = {
    "E101": {
        "name": "Ravi",
        "department": "IT",
        "salary": 50000
    },
    "E102": {
        "name": "Priya",
        "department": "HR",
        "salary": 45000
    },
    "E103": {
        "name": "Kiran",
        "department": "IT",
        "salary": 60000
    },
    "E104": {
        "name": "Sneha",
        "department": "Finance",
        "salary": 55000
    },
    "E105": {
        "name": "Arjun",
        "department": "IT",
        "salary": 40000
    }
}


# Tool 1: Get employee details
@tool
def get_employee_details(employee_id: str) -> str:
    """Get employee details using employee ID."""

    employee = employees.get(employee_id)

    if employee:
        return str(employee)

    return "Employee not found."


# Tool 2: Calculate annual salary
@tool
def calculate_annual_salary(employee_id: str) -> str:
    """Calculate annual salary of an employee."""

    employee = employees.get(employee_id)

    if employee:
        annual_salary = employee["salary"] * 12

        return f"Annual Salary: Rs. {annual_salary}"

    return "Employee not found."


# Tool 3: Find employees by department
@tool
def get_employees_by_department(department: str) -> str:
    """Find all employees belonging to a department."""

    result = []

    for emp_id, emp in employees.items():

        if emp["department"].lower() == department.lower():

            result.append(
                f"{emp_id} - {emp['name']}"
            )

    if result:
        return "\n".join(result)

    return "No employees found in this department."


# Tool 4: Count employees
@tool
def count_employees() -> str:
    """Return the total number of employees."""

    return f"Total employees: {len(employees)}"


# Tool 5: Calculate employee bonus
@tool
def calculate_bonus(employee_id: str) -> str:
    """Calculate employee bonus as 10 percent of annual salary."""

    employee = employees.get(employee_id)

    if employee:

        annual_salary = employee["salary"] * 12

        bonus = annual_salary * 0.10

        return f"Employee Bonus: Rs. {bonus:.2f}"

    return "Employee not found."