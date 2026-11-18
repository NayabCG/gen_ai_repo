
from dotenv import load_dotenv

from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# Initialize embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# Initialize LLM
llm = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)


# Create prompt template
prompt = ChatPromptTemplate.from_template("""
You are an HR Policy Assistant.

Answer the employee's question using only
the information available in the context.

If the answer is not available in the context,
respond with:
"I could not find this information in the uploaded documents."

Context:
{context}

Question:
{question}

Answer:
""")


# Create RAG chain
rag_chain = prompt | llm | StrOutputParser()


# Create vector database
def create_vector_store(chunks):

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        collection_name="hr_policy"
    )

    return vector_store


# Retrieve documents and generate answer
def ask_question(vector_store, question):

    retriever = vector_store.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 3}
    )

    # Retrieve relevant chunks
    retrieved_docs = retriever.invoke(question)

    # Combine retrieved content
    context = "\n\n".join(
        doc.page_content
        for doc in retrieved_docs
    )

    # Generate answer
    answer = rag_chain.invoke({
        "context": context,
        "question": question
    })

    return answer, retrieved_docs
