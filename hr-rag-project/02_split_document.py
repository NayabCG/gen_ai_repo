
from pathlib import Path
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Load document
text = Path("data/hr_policy.txt").read_text(encoding="utf-8")

document = Document(
    page_content=text,
    metadata={"source": "hr_policy.txt"}
)

# Create text splitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)

# Split document
chunks = text_splitter.split_documents([document])

print("Total chunks:", len(chunks))

# Display chunks
for index, chunk in enumerate(chunks):

    print(f"\nChunk {index + 1}")
    print(chunk.page_content)

    print("Metadata:", chunk.metadata)
