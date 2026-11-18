Test 1: Retrieve all employees

USER INPUT

Show all employees.

AGENT SELECTS

get_all_employees()

EXPECTED RESULT
The database contains five employees:
- Ravi – IT – ₹50,000
- Priya – HR – ₹45,000
- Kiran – IT – ₹60,000
- Sneha – Finance – ₹55,000
- Arjun – IT – ₹40,000


Test 2: Search employee

USER INPUT

Find employee E103.

AGENT SELECTS

get_employee_by_id("E103")

EXPECTED RESULT
Employee Name: Kiran

Employee ID: E103

Department: IT

Salary: ₹60,000


Test 3: Department search

USER INPUT

Show all employees working in IT.

AGENT SELECTS

get_employees_by_department("IT")

EXPECTED RESULT
IT Department Employees:
1. Ravi – ₹50,000
2. Kiran – ₹60,000
3. Arjun – ₹40,000


Test 4: Highest salary

USER INPUT

Who is getting the highest salary?

AGENT SELECTS

execute_readonly_sql()

LLM GENERATES SQL
SELECT name, salary
FROM Employee
ORDER BY salary DESC
LIMIT 1;


EXPECTED RESULT
Kiran is the highest-paid employee with a monthly salary of ₹60,000.

Test 5: Average salary

USER INPUT

What is the average salary of employees?

LLM GENERATES SQL
SELECT AVG(salary)
FROM Employee;


EXPECTED RESULT
Average monthly salary: ₹50,000.