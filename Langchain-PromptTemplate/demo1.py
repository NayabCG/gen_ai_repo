from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.7,
    max_completion_tokens=500
)

prompt=ChatPromptTemplate.from_template(
     """
    Explain {topic} to a {level} developer.

    Use simple language.
    Include one example.
    """
)

messages=prompt.invoke({
    "topic":'What is LLM',
    "level":'beginner'
})
response=model.invoke(messages)
print(response.content)