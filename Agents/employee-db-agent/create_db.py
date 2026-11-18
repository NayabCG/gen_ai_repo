import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("company.db")

cursor = conn.cursor()

# Create Employee table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    employee_id TEXT PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

# Insert sample records
employees = [
    ("E101", "Ravi", "IT", 50000),
    ("E102", "Priya", "HR", 45000),
    ("E103", "Kiran", "IT", 60000),
    ("E104", "Sneha", "Finance", 55000),
    ("E105", "Arjun", "IT", 40000)
]

cursor.executemany("""
INSERT OR IGNORE INTO Employee
(employee_id, name, department, salary)
VALUES (?, ?, ?, ?)
""", employees)

conn.commit()

conn.close()

print("Database created successfully!")