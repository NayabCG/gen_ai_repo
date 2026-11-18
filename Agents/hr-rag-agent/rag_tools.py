from dotenv import load_dotenv

from langchain.tools import tool

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

load_dotenv()


# Step 1: Initialize embeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# Step 2: Load existing vector store

vector_store = FAISS.load_local(
    "vector_store",
    embeddings,
    allow_dangerous_deserialization=True
)


# Step 3: Create RAG retrieval tool

@tool
def search_hr_documents(question: str) -> str:
    """
    Search HR policy and company documents
    to retrieve information relevant to a question.
    """

    # Search relevant document chunks
    results = vector_store.similarity_search(
        question,
        k=4
    )

    if not results:
        return "No relevant information found."

    # Prepare retrieved context
    context = []

    for doc in results:

        source = doc.metadata.get(
            "source", "Unknown"
        )

        page = doc.metadata.get("page")

        context.append(
            f"""
            Source: {source}
            Page: {page}

            Content:
            {doc.page_content}
            """
        )

    return "\n\n".join(context)