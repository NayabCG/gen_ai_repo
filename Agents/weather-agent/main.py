from dotenv import load_dotenv

from langchain.agents import create_agent
from langchain_openai import ChatOpenAI

from weather_tools import get_current_weather

# Load environment variables
load_dotenv()

# Initialize LLM
model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

# Register external API tool
tools = [
    get_current_weather
]

# Create AI Agent
agent = create_agent(
    model=model,
    tools=tools,
    system_prompt="""
    You are a Weather Information AI Assistant.

    Help users retrieve current weather
    information for different cities.

    Use the weather tool whenever the user
    asks about current weather.

    Explain temperature in Celsius,
    humidity in percentage and wind speed
    in km/h.

    If the location is not found,
    inform the user.

    Do not invent weather information.
    """
)

print("Weather AI Agent Started!")

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