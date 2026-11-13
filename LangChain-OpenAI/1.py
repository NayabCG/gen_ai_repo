from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
# Initialize the ChatOpenAI model
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.3,
    api_key=os.getenv('OPENAI_API_KEY')
)
# Invoke the model with a prompt
response=model.invoke('Who is India PM,short answer')
# Print the response
print(response.content)