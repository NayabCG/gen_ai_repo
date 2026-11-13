from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.7,
    max_completion_tokens=500
)
# create a prompt template for the chat model
# with system and human messages
prompt=ChatPromptTemplate.from_messages([
    ('system','You are an experienced Python instructor'),
    ('human','Explain {topic} to a {level} developer')
    
])

messages=prompt.invoke({
    "topic":'What is LLM',
    "level":'beginner'
})
response=model.invoke(messages)
print(response.content)