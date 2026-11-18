from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from tools import (
    get_employee_details,
    calculate_annual_salary,
    get_employees_by_department,
    count_employees,
    calculate_bonus
)

# Load environment variables
load_dotenv()

# Initialize LLM
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

# Register all five tools
tools = [
    get_employee_details,
    calculate_annual_salary,
    get_employees_by_department,
    count_employees,
    calculate_bonus
]

# Create Agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are an Employee Management AI Assistant.

    Help users with employee information,
    salary calculations, department searches,
    employee counts and bonus calculations.

    Select the appropriate tool based on
    the user's request.

    Use tools whenever required.
    Never invent employee information.

    Bonus is calculated as 10 percent
    of annual salary.
    """
)

print("Employee Management AI Agent Started!")

# User interaction
while True:

    user_input = input("\nAsk your question: ")

    if user_input.lower() == "exit":
        print("Agent stopped.")
        break

    response = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    print("\nAI Agent Response:")

    print(response["messages"][-1].content)