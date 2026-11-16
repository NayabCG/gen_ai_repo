from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
load_dotenv()
class TopicExplanation(BaseModel):
    topic:str
    difficulty:str
    summary:str
    key_points:list[str]
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an experienced programming instructor."
    ),
    (
        "human",
        """
        Explain {topic} for a {level} developer in short.
        """
    )
])
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.3,
    openai_api_key=os.environ.get('OPENAI_API_KEY')
)
structured_model=model.with_structured_output(
    TopicExplanation
)
chain=prompt | structured_model
result=chain.invoke({
    'topic':'FastAPI',
    'level':'beginner'
})
print(result)