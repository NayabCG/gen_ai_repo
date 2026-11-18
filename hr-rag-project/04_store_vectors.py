
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma

load_dotenv()

# Load document
text = Path("data/hr_policy.txt").read_text(encoding="utf-8")

document = Document(
    page_content=text,
    metadata={"source": "hr_policy.txt"}
)

# Split document
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

chunks = text_splitter.split_documents([document])

# Initialize embeddings
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small"
)

# Create Chroma vector database
vector_store = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    collection_name="hr_policy"
)

print("Vectors stored successfully!")

print("Total documents stored:", len(chunks))
