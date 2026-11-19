from pathlib import Path

from dotenv import load_dotenv

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS


load_dotenv()


def create_vector_store():

    documents = []

    docs_folder = Path("docs")

    # Load documents
    for file_path in docs_folder.iterdir():

        if file_path.suffix.lower() == ".pdf":

            loader = PyPDFLoader(str(file_path))

            documents.extend(loader.load())

        elif file_path.suffix.lower() == ".txt":

            loader = TextLoader(
                str(file_path),
                encoding="utf-8"
            )

            documents.extend(loader.load())

    if not documents:
        raise ValueError("No documents found in docs folder.")

    print("Documents loaded:", len(documents))

    # Split documents
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    print("Chunks created:", len(chunks))

    # Create embeddings
    embeddings = OpenAIEmbeddings(
        model="text-embedding-3-small"
    )

    # Create FAISS database
    vector_store = FAISS.from_documents(
        chunks,
        embeddings
    )

    # Save vector database
    vector_store.save_local("vector_store")

    print("Vector store created successfully!")


if __name__ == "__main__":

    create_vector_store()