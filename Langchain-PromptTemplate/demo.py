from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.7,
    max_completion_tokens=500
)
# create a prompt template for the chat model
prompt=ChatPromptTemplate.from_template(
     """
    You are a Python instructor.

    Explain the following topic:
    {topic} in 5 simple points in short.

    Target audience:
    {audience}
    """
)
# invoke the prompt template with the topic and audience
messages=prompt.invoke({
    "topic":'What is LLM',
    "audience":'beginner python developers'
})
# invoke the model with the messages
response=model.invoke(messages)
print(response.content)