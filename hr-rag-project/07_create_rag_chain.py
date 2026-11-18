
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)

# Create prompt template
prompt = ChatPromptTemplate.from_template("""
You are an HR Policy Assistant.

Answer using only the provided context.

If the answer is not available in the context,
say that the information is not available.

Context:
{context}

Question:
{question}

Answer:
""")

# Create chain
rag_chain = prompt | llm | StrOutputParser()

# Test with sample context
response = rag_chain.invoke({
    "context": """
    Employees are eligible for 12 casual leaves per year.
    """,
    "question": "How many casual leaves are available?"
})

print("Answer:")
print(response)
