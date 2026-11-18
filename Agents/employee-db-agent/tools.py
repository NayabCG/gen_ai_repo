from langchain.tools import tool
from database import get_connection


# Tool 1: Get all employees
@tool
def get_all_employees() -> str:
    """Retrieve all employees from the database."""

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM Employee
    """)

    records = cursor.fetchall()

    conn.close()

    return str(records)


# Tool 2: Get employee by ID
@tool
def get_employee_by_id(employee_id: str) -> str:
    """Retrieve employee details using employee ID."""

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM Employee
        WHERE employee_id = ?
    """, (employee_id,))

    record = cursor.fetchone()

    conn.close()

    if record:
        return str(record)

    return "Employee not found."


# Tool 3: Get employees by department
@tool
def get_employees_by_department(department: str) -> str:
    """Retrieve employees belonging to a particular department."""

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM Employee
        WHERE department = ?
    """, (department,))

    records = cursor.fetchall()

    conn.close()

    return str(records)


# Tool 4: Execute read-only SQL queries
@tool
def execute_readonly_sql(query: str) -> str:
    """Execute a read-only SELECT SQL query on the Employee table.
    Use this for salary aggregations, sorting, counting and other
    employee data analysis. Only SELECT queries are permitted."""

    query = query.strip().rstrip(";").strip()

    if not (
        query.upper().startswith("SELECT ")
        or query.upper().startswith("WITH ")
    ):
        return "Only SELECT queries are permitted."

    try:

        conn = get_connection()

        # Prevent database modifications
        conn.execute("PRAGMA query_only = ON")

        cursor = conn.cursor()

        cursor.execute(query)

        records = cursor.fetchall()

        conn.close()

        return str(records)

    except Exception as e:

        return f"Database query failed: {e}"