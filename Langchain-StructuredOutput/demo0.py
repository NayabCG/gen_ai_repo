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

response = model.invoke("""
Extract employee information from the following text:

Virat is 37 years old.
He works primarily with Python.
He has 10 years of experience.
""")
# print the response in structured format
print(response.content)