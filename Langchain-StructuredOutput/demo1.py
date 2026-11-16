from pydantic import BaseModel, Field
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)
# Define the structure for the employee information
class Employee(BaseModel):
    name: str = Field(description="Employee name")
    age: int = Field(description="Employee age")
    technology: str = Field(description="Primary technology")
    experience: int = Field(description="Experience in years")
# Create a structured model using the Employee class
# model.with_structured_output(Employee) creates a structured output model based 
# on the Employee class. This allows the model to return responses in a 
# structured format that matches the fields defined in the Employee class.
structured_model = model.with_structured_output(Employee)

# Invoke the structured model with a prompt to extract employee information
response = structured_model.invoke("""
Extract employee information from the following text:

Virat is 37 years old.
He works primarily with Python.
He has 10 years of experience.
""")
# print the response in structured format
print(response)