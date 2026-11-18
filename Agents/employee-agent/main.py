from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from tools import (
    get_employee_details,
    calculate_annual_salary
)

# Load environment variables
load_dotenv()

# Initialize LLM
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

# Register tools
tools = [
    get_employee_details,
    calculate_annual_salary
]

# Create AI Agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are an Employee Information Assistant.

    Help users retrieve employee details
    and calculate annual salaries.

    Use the available tools whenever required.
    Do not make up employee information.
    """
)

print("Employee AI Agent Started!")

while True:

    user_input = input("\nAsk your question: ")

    if user_input.lower() == "exit":
        print("Agent stopped.")
        break
    # Invoke the agent with user input
    response = agent.invoke({
        "messages": [
            {"role": "user", "content": user_input}
        ]
    })

    print("\nAI Agent Response:")
    # Print the last message from the response
    print(response["messages"][-1].content)