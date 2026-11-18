from langchain.tools import tool

# Sample employee data
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
    }
}


@tool
def get_employee_details(employee_id: str) -> str:
    # docstring(explain what the tool does)
    """Retrieve employee details using employee ID."""

    employee = employees.get(employee_id)

    if employee:
        return (
            f"Name: {employee['name']}, "
            f"Department: {employee['department']}, "
            f"Monthly Salary: {employee['salary']}"
        )

    return "Employee not found."


@tool
def calculate_annual_salary(employee_id: str) -> str:
    """Calculate annual salary using employee ID."""

    employee = employees.get(employee_id)

    if employee:
        annual_salary = employee["salary"] * 12
        return f"Annual salary is Rs. {annual_salary}"

    return "Employee not found."