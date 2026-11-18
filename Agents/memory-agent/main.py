from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from langgraph.checkpoint.memory import InMemorySaver


# Load environment variables
load_dotenv()


# Initialize LLM
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)


# Create memory checkpointer
memory = InMemorySaver()


# Create AI Agent
agent = create_agent(
    model=model,
    tools=[],
    checkpointer=memory,
    system_prompt="""
    You are a Personal AI Assistant.

    Remember the information shared by
    the user during the conversation.

    Use previous conversation messages
    to answer follow-up questions.

    Do not invent personal information.

    If the user has not shared information,
    clearly say that you don't know.
    """
)


# Create conversation ID
config = {
    "configurable": {
        "thread_id": "user_101"
    }
}


print("AI Agent with Memory Started!")


while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":

        print("Agent stopped.")

        break


    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        },
        config=config
    )


    print("\nAI Agent:")

    print(response["messages"][-1].content)