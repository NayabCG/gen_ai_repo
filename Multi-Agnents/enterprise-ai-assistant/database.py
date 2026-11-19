import sqlite3


DB_NAME = "company.db"


def get_connection():

    return sqlite3.connect(DB_NAME)


def initialize_database():

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee (
            employee_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            department TEXT NOT NULL,
            salary REAL NOT NULL
        )
    """)

    employees = [
        ("E101", "Ravi", "IT", 50000),
        ("E102", "Priya", "HR", 45000),
        ("E103", "Kiran", "Finance", 60000),
        ("E104", "Sneha", "IT", 55000),
        ("E105", "Arjun", "Finance", 40000)
    ]

    cursor.executemany("""
        INSERT OR IGNORE INTO Employee
        VALUES (?, ?, ?, ?)
    """, employees)

    conn.commit()

    conn.close()


def get_employee(employee_id: str):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute("""
        SELECT employee_id, name, department, salary
        FROM Employee
        WHERE employee_id = ?
    """, (employee_id,))

    result = cursor.fetchone()

    conn.close()

    return result