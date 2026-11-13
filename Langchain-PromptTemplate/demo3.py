from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.7,
    max_completion_tokens=500
)


prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an experienced programming instructor.

        Explain concepts clearly.
        Use practical examples.
        """
    ),
    (
        "human",
        """
        Explain {topic}.

        Programming language: {language}
        Experience level: {level}

        Include:
        1. Definition
        2. Explanation
        3. Code example
        4. Real-world use case
        """
    )
])

messages = prompt.invoke({
    "topic": "Dependency Injection",
    "language": "Python",
    "level": "beginner"
})


response = model.invoke(messages)

print(response.content)