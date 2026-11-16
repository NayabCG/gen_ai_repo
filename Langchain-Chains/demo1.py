from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
load_dotenv()
prompt=ChatPromptTemplate.from_template(
    'Explain {topic} in sample terms with in 100 words'
)
model=ChatOpenAI(
    model='gpt-5.5',
    temperature=0.3,
    openai_api_key=os.environ.get('OPENAI_API_KEY')
)
parser=StrOutputParser() # The parser converts the AIMessage into normal python string
# create a chain that combines the prompt, model and parser
chain=prompt | model | parser
result=chain.invoke({
    'topic':'Python decorators'
})
print(result)