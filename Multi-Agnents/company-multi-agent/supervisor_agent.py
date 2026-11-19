from dotenv import load_dotenv

from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI
from hr_agent import hr_agent
from finance_agent import finance_agent
from it_agent import it_agent



# Load environment variables
load_dotenv()


# Initialize Supervisor LLM
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)


# Tool 1: HR Agent
@tool
def ask_hr_agent(question: str) -> str:
    """Delegate HR policy and employee leave questions to the HR specialist."""

    response = hr_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    return response["messages"][-1].content


# Tool 2: Finance Agent
@tool
def ask_finance_agent(question: str) -> str:
    """Delegate salary and financial calculation questions to the Finance specialist."""

    response = finance_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    return response["messages"][-1].content


# Tool 3: IT Agent
@tool
def ask_it_agent(question: str) -> str:
    """Delegate technical support and password reset questions to the IT specialist."""

    response = it_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": question
            }
        ]
    })

    return response["messages"][-1].content


# Register specialized Agents as tools
supervisor_tools = [
    ask_hr_agent,
    ask_finance_agent,
    ask_it_agent
]


# Create Supervisor Agent
supervisor_agent = create_agent(
    model=model,
    tools=supervisor_tools,
    system_prompt="""
    You are the Supervisor Agent of a company AI assistant.

    You coordinate the following specialized Agents:

    1. HR Agent:
       Handles leave policies and HR questions.

    2. Finance Agent:
       Handles salary calculations and financial questions.

    3. IT Support Agent:
       Handles technical issues and password support.

    Instructions:

    - Understand the user's request.
    - Select the appropriate specialist.
    - Delegate questions using the available tools.
    - For questions involving multiple departments,
      invoke all relevant specialist Agents.
    - Combine their results into one clear response.
    - Do not invent information.
    """
)


# Start application
print("Company Multi-Agent System Started!")

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":

        print("Application stopped.")

        break

    response = supervisor_agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": user_input
            }
        ]
    })

    print("\nCompany AI Assistant:")

    print(response["messages"][-1].content)