from langchain.tools import tool
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


# Initialize model
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)
# IT Support Tool
@tool
def get_password_reset_steps() -> str:
    """Provide company password reset instructions."""

    return """
    Password Reset Instructions:

    1. Open the company login portal.
    2. Click Forgot Password.
    3. Enter your registered email address.
    4. Verify your identity using the
       company-approved verification method.
    5. Create a new password.

    Contact the IT helpdesk if the process fails.
    """


# Create IT Support Agent
it_agent = create_agent(
    model=model,
    tools=[get_password_reset_steps],
    system_prompt="""
    You are an IT Support Specialist Agent.

    Handle technical support questions.

    Use the available IT support tool
    whenever required.

    Provide clear troubleshooting steps.

    Do not invent company IT procedures.
    """
)