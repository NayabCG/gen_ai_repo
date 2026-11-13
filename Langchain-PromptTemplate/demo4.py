from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.7,
    max_completion_tokens=1000
)

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an expert programming instructor.

        Explain concepts clearly and practically.
        """
    ),
    (
        "human",
        """
        Explain {topic}.

        Language: {language}
        Level: {level}

        Include a code example.
        """
    )
])



def explain_topic(
    topic: str,
    language: str,
    level: str
):

    messages = prompt.invoke({
        "topic": topic,
        "language": language,
        "level": level
    })

    response = model.invoke(messages)

    return response.content


answer = explain_topic(
    topic="Decorators",
    language="Python",
    level="beginner"
)

print(answer)