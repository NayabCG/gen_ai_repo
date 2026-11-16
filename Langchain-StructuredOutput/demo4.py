# Prompt + Structured Output
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

# Define a Pydantic model for the structured output
class TopicExplanation(BaseModel):

    topic: str
    difficulty: str
    summary: str
    key_points: list[str]

# Define a prompt template for explaining programming topics
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        You are an experienced programming instructor.
        Explain programming topics clearly.
        """
    ),
    (
        "human",
        """
        Explain the following topic:

        Topic: {topic}

        Experience level: {level}
        """
    )
])


model = ChatOpenAI(
    model="gpt-5.5",
    temperature=0.3,
    max_completion_tokens=1000,
    api_key=os.getenv("OPENAI_API_KEY")
)

# Create a structured model using the TopicExplanation class
structured_model = model.with_structured_output(
    TopicExplanation
)

# Invoke the prompt with a topic and level, then pass the result to the structured model
messages = prompt.invoke({
    "topic": "Python decorators",
    "level": "beginner"
})

# Invoke the structured model with the messages from the prompt
result = structured_model.invoke(messages)

print(result)