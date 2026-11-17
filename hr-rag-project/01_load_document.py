
from pathlib import Path
from langchain_core.documents import Document

# Read the text file
file_path = Path("data/hr_policy.txt")

text = file_path.read_text(encoding="utf-8")

# Convert into LangChain Document
document = Document(
    page_content=text,
    metadata={"source": "hr_policy.txt"}
)

print("Document loaded successfully!")

print("\nDocument Content:")
print(document.page_content)

print("\nMetadata:")
print(document.metadata)
