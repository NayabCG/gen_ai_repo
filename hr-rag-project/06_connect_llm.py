
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

# Send a question directly to LLM
response = llm.invoke(
    "What is Artificial Intelligence?"
)

print("LLM Response:")
print(response.content)
