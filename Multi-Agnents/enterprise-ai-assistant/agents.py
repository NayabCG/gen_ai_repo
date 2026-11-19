from langchain.agents import create_agent
from langchain.tools import tool

from langchain_openai import ChatOpenAI

from tools import (
    search_company_documents,
    get_employee_financial_details,
    get_it_support_information,
    get_weather
)


# Initialize model
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)


# =====================================
# HR SPECIALIST AGENT
# =====================================

hr_agent = create_agent(
    model=model,
    tools=[
        search_company_documents
    ],
    system_prompt="""
    You are an HR Specialist Agent.

    Handle HR policy and company document questions.

    Use the document search tool to retrieve information.

    Answer only using retrieved document information.

    Mention the document source when available.

    If information is unavailable, say so clearly.
    """
)


# =====================================
# FINANCE SPECIALIST AGENT
# =====================================

finance_agent = create_agent(
    model=model,
    tools=[
        get_employee_financial_details
    ],
    system_prompt="""
    You are a Finance Specialist Agent.

    Handle employee salary and financial information.

    Retrieve actual employee information
    using the database tool.

    Do not invent employee salary information.

    Only return information retrieved
    from the database.
    """
)


# =====================================
# IT SUPPORT SPECIALIST AGENT
# =====================================

it_agent = create_agent(
    model=model,
    tools=[
        get_it_support_information
    ],
    system_prompt="""
    You are an IT Support Specialist Agent.

    Handle technical support questions.

    Use the IT support tool to retrieve
    troubleshooting information.

    Explain the steps clearly.
    """
)


# =====================================
# GENERAL INFORMATION AGENT
# =====================================

general_agent = create_agent(
    model=model,
    tools=[
        get_weather
    ],
    system_prompt="""
    You are a General Information Agent.

    Handle general information and weather questions.

    Use the weather tool for current weather requests.

    Do not invent live weather information.
    """
)


# =====================================
# SUPERVISOR AGENT
# =====================================

@tool
def delegate_to_hr_agent(question: str) -> str:
    """Delegate HR policy and company document questions to the HR Agent."""

    response = hr_agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    return response["messages"][-1].content


@tool
def delegate_to_finance_agent(question: str) -> str:
    """Delegate employee salary and finance questions to the Finance Agent."""

    response = finance_agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    return response["messages"][-1].content


@tool
def delegate_to_it_agent(question: str) -> str:
    """Delegate technical support questions to the IT Agent."""

    response = it_agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    return response["messages"][-1].content


@tool
def delegate_to_general_agent(question: str) -> str:
    """Delegate general information and weather questions to the General Agent."""

    response = general_agent.invoke({
        "messages": [
            {"role": "user", "content": question}
        ]
    })

    return response["messages"][-1].content


# =====================================
# CREATE SUPERVISOR
# =====================================

def create_supervisor(checkpointer):

    supervisor = create_agent(
        model=model,
        tools=[
            delegate_to_hr_agent,
            delegate_to_finance_agent,
            delegate_to_it_agent,
            delegate_to_general_agent
        ],
        checkpointer=checkpointer,
        system_prompt="""
        You are the Supervisor Agent of an
        Enterprise AI Assistant.

        You coordinate four specialized Agents.

        HR Agent:
        Handles company policies, HR documents
        and employee leave information.

        Finance Agent:
        Handles employee salary information.

        IT Agent:
        Handles technical support questions.

        General Agent:
        Handles weather and general information.

        Instructions:

        1. Understand the user's question.

        2. Delegate the question to the
           appropriate specialized Agent.

        3. If a question involves multiple
           domains, invoke all relevant Agents.

        4. Combine the returned results.

        5. Provide one clear final response.

        6. Do not invent information.

        7. Do not expose information from
           one employee to another.

        8. Ask for clarification if required.
        """
    )

    return supervisor