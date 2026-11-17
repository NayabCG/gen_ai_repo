
from io import BytesIO

from pypdf import PdfReader
from docx import Document as DocxDocument

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


def load_uploaded_document(uploaded_file):

    file_name = uploaded_file.name
    file_extension = file_name.split(".")[-1].lower()

    file_bytes = uploaded_file.getvalue()

    # Read PDF
    if file_extension == "pdf":

        pdf_reader = PdfReader(BytesIO(file_bytes))

        text = "\n".join(
            page.extract_text() or ""
            for page in pdf_reader.pages
        )

    # Read TXT
    elif file_extension == "txt":

        text = file_bytes.decode("utf-8")

    # Read DOCX
    elif file_extension == "docx":

        doc = DocxDocument(BytesIO(file_bytes))

        text = "\n".join(
            paragraph.text
            for paragraph in doc.paragraphs
        )

    else:
        raise ValueError("Unsupported file format")

    if not text.strip():
        raise ValueError(
            f"No readable text found in {file_name}"
        )

    document = Document(
        page_content=text,
        metadata={"source": file_name}
    )

    return document


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = text_splitter.split_documents(documents)

    return chunks
