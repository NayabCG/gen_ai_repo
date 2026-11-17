
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_chroma import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


# STEP 1: Load document
text = Path("data/hr_policy.txt").read_text(encoding="utf-8")

document = Document(
    page_content=text,
    metadata={"source": "hr_policy.txt"}
)

print("Document loaded!")


# STEP 2: Split document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_documents([document])

print("Document split into chunks:", len(chunks))


# STEP 3: Initialize embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# STEP 4: Store vectors
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="hr_policy"
)

print("Vectors stored successfully!")


# STEP 5: Create retriever
retriever = vector_store.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 3}
)


# STEP 6: Initialize LLM
llm = ChatOpenAI(
    model="gpt-5.5",
    temperature=0
)


# STEP 7: Create prompt template
prompt = ChatPromptTemplate.from_template("""
You are an HR Policy Assistant.

Answer the employee's question using only
the information provided in the context.

If the answer is not available in the context,
say:
"I could not find this information in the HR policy document."

Context:
{context}

Question:
{question}

Answer:
""")


# STEP 8: Create RAG chain
rag_chain = prompt | llm | StrOutputParser()


# STEP 9: Define question-answering function
def ask_hr_question(question):

    # Retrieve relevant chunks
    retrieved_docs = retriever.invoke(question)

    # Combine retrieved content
    context = "\n\n".join(
        doc.page_content for doc in retrieved_docs
    )

    # Generate answer
    answer = rag_chain.invoke({
        "context": context,
        "question": question
    })

    return answer


# STEP 10: Interactive application
print("\n===== HR POLICY ASSISTANT =====")

while True:

    question = input("\nAsk your question (exit to stop): ")

    if question.lower() == "exit":
        print("Thank you!")
        break

    answer = ask_hr_question(question)

    print("\nAI Answer:")
    print(answer)
