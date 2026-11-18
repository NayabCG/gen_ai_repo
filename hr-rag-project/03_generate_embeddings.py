
from pathlib import Path
from dotenv import load_dotenv

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings

# Load environment variables
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

# Initialize embedding model
embeddings = OpenAIEmbeddings(
    model="text-embedding-3-small",
    # api_key=os.getenv("OPENAI_API_KEY")
)

# Generate embedding for first chunk
vector = embeddings.embed_query(
    chunks[0].page_content
)

print("Embedding generated successfully!")

print("Vector dimensions:", len(vector))

print("First 10 values:", vector[:10])
