import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0,
    api_key=os.getenv("OPENAI_API_KEY")
)
# Define the structure for the employee using a JSON schema
schema = {
    "title": "Employee",
    "description": "Employee information",
    "type": "object",
    "properties": {
        "name": {
            "type": "string"
        },
        "age": {
            "type": "integer"
        },
        "technology": {
            "type": "string"
        },
        "experience": {
            "type": "integer"
        }
    },
    "required": [
        "name",
        "age",
        "technology",
        "experience"
    ],
    "additionalProperties": False
}
# Create a structured model using the JSON schema
structured_model = model.with_structured_output(schema)

# Invoke the structured model with a prompt to extract employee information
response = structured_model.invoke("""
Extract employee information:

Ramesh is 35 years old.
He works with Angular.
He has 10 years of experience.
""")
# print the response in structured dictionary format
print(response)