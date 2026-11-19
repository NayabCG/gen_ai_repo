from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


# Initialize model
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

# Finance Tool
@tool
def calculate_annual_salary(
    monthly_salary: float
) -> str:
    """Calculate annual salary from monthly salary."""

    annual_salary = monthly_salary * 12

    return (
        f"Monthly Salary: Rs. {monthly_salary}\n"
        f"Annual Salary: Rs. {annual_salary}"
    )


# Create Finance Agent
finance_agent = create_agent(
    model=model,
    tools=[calculate_annual_salary],
    system_prompt="""
    You are a Finance Specialist Agent.

    Handle salary and financial calculations.

    Use the calculation tool when required.

    Explain calculations clearly.

    Do not invent employee salary information.
    """
)