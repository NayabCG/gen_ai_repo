from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


# Initialize model
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)


# HR Tool
@tool
def get_leave_policy() -> str:
    """Retrieve company employee leave policy."""

    return """
    Company Leave Policy:

    Casual Leave: 12 days per year.
    Sick Leave: 10 days per year.
    Earned Leave: 15 days per year.

    All leave requests require
    manager approval.
    """


# Create HR Agent
hr_agent = create_agent(
    model=model,
    tools=[get_leave_policy],
    system_prompt="""
    You are an HR Specialist Agent.

    Handle only HR-related questions.

    Use the leave policy tool when required.

    Explain company policies in simple language.

    Do not invent company policies.
    """
)