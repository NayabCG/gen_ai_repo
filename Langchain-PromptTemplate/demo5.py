from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.7,
    max_completion_tokens=500
)


explain_prompt = ChatPromptTemplate.from_template(
    "Explain {topic} to a beginner in 50 words"
)


quiz_prompt = ChatPromptTemplate.from_template(
    "Create 5 MCQs about {topic}."
)


topic = "Python decorators"


messages = explain_prompt.invoke({
    "topic": topic
})

response = model.invoke(messages)

print("EXPLANATION")
print(response.content)


messages = quiz_prompt.invoke({
    "topic": topic
})

response = model.invoke(messages)

print("\nQUIZ")
print(response.content)