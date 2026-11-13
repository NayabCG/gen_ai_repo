from langchain_openai import ChatOpenAI
from langchain_core.messages import (SystemMessage,HumanMessage,AIMessage)
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.3
)
# messages are used to store the conversation history between the user and the AI model. 
# The SystemMessage is used to set the context for the conversation, 
# while HumanMessage and AIMessage are used to represent the user's input and the AI's response, respectively.
messages=[
    SystemMessage(
        content='You are a helpful  assistant'
    )
]
while True:
    user_input=input('\n You:')
    if user_input.lower()=='exit':
        break
    messages.append(HumanMessage(content=user_input))
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.content))
    # print(type(response))
    print('\nAI:',response.content)