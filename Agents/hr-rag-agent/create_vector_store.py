from pathlib import Path

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader
)

from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_openai import OpenAIEmbeddings

from langchain_community.vectorstores import FAISS

# Step 1: Read documents
documents = []

docs_folder = Path("docs")

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


print("Documents loaded:", len(documents))


# Step 2: Split documents into chunks

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print("Total chunks created:", len(chunks))


# Step 3: Generate embeddings

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)


# Step 4: Create FAISS vector store

vector_store = FAISS.from_documents(
    chunks,
    embeddings
)


# Step 5: Save vector store

vector_store.save_local("vector_store")

print("Vector store created successfully!")