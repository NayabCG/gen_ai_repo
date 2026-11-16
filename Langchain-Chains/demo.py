from langchain_core.prompts import ChatPromptTemplate
from langchain_openai  import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

prompt=ChatPromptTemplate.from_template(
    'Explain {topic} in simple terms with in 100 words'
)
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.3,
    openai_api_key=os.environ.get('OPENAI_API_KEY')
)
# create a chain that combines the prompt and the model
chain=prompt|model
result=chain.invoke({
    'topic':'FastAPI'
})
print(result.content)