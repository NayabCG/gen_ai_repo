from typing_extensions import TypedDict
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)
# Define the structure for the employee information using TypedDict
class Employee(TypedDict):
    name: str
    age: int
    technology: str
    experience: int
# Create a structured model using the Employee TypedDict
structured_model = model.with_structured_output(Employee)

# Invoke the structured model with a prompt to extract employee information
response = structured_model.invoke("""
Extract employee information:

Ravi is 30 years old.
He works with .NET.
He has 8 years of experience.
""")
# print the response in structured dictionary format
print(response)