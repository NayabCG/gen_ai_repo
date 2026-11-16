from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
prompt=ChatPromptTemplate.from_template(
    'Give a one-line definition of {topic}'
)
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.3,
    openai_api_key=os.environ.get('OPENAI_API_KEY')
)
parser=StrOutputParser()
def add_prefix(text:str)->str:
    return 'AI Explanation: '+text
prefix_runnable=RunnableLambda(add_prefix)
chain=(
    prompt | model | parser | prefix_runnable
)
result=chain.invoke({
    'topic':'Dependency Injection'
})
print(result)