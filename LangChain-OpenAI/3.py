from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

from openai import api_key
load_dotenv()
# Initialize the ChatOpenAI model
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.3,
    max_completion_tokens=500,
    api_key=os.getenv('OPENAI_API_KEY')
)
while True:
    prompt=input("Enter your prompt: ")
    if prompt.lower() == 'exit':
        print("Exiting the program.")
        break
    # Invoke the model with a prompt
    response=model.invoke(prompt)
    # Print the response
    print(response.content)
   
