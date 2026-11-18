from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from tools import (
    get_all_employees,
    get_employee_by_id,
    get_employees_by_department,
    execute_readonly_sql
)

# Load environment variables
load_dotenv()

# Initialize LLM
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

# Register database tools
tools = [
    get_all_employees,
    get_employee_by_id,
    get_employees_by_department,
    execute_readonly_sql
]

# Create AI Agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are an Employee Database AI Assistant.

    You can retrieve employee information
    from the SQLite database.

    Available database table:

    Employee:
    - employee_id
    - name
    - department
    - salary

    Instructions:

    1. Use appropriate database tools to
       answer employee-related questions.

    2. Use get_all_employees to retrieve
       all employee records.

    3. Use get_employee_by_id to retrieve
       a particular employee.

    4. Use get_employees_by_department
       to search by department.

    5. Use execute_readonly_sql for
       aggregate queries such as COUNT,
       MAX, MIN, AVG and sorting.

    6. Only retrieve information.
       Never attempt to modify the database.

    7. Do not invent employee information.

    8. Explain database results in simple
       natural language.
    """
)

print("Employee Database AI Agent Started!")

while True:

    user_input = input("\nAsk your question: ")

    if user_input.lower() == "exit":
        print("Agent stopped.")
        break

    response = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })

    print("\nAI Agent Response:")

    print(response["messages"][-1].content)