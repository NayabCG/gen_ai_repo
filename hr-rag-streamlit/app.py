
import streamlit as st

from document_processor import (
    load_uploaded_document,
    split_documents
)

from rag_pipeline import (
    create_vector_store,
    ask_question
)


# Page configuration
st.set_page_config(
    page_title="HR Policy Assistant",
    page_icon="🏢",
    layout="wide"
)


# Application title
st.title("🏢 HR Policy Assistant")

st.write(
    "Upload your HR policy documents and "
    "ask questions using AI."
)


# Initialize session state
if "vector_store" not in st.session_state:
    st.session_state.vector_store = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


# Sidebar
with st.sidebar:

    st.header("📄 Upload Documents")

    uploaded_files = st.file_uploader(
        "Upload your HR documents",
        type=["pdf", "txt", "docx"],
        accept_multiple_files=True
    )

    if st.button("Process Documents", type="primary"):

        if not uploaded_files:

            st.warning("Please upload documents first.")

        else:

            try:

                with st.spinner("Processing documents..."):

                    # Load documents
                    documents = [
                        load_uploaded_document(file)
                        for file in uploaded_files
                    ]

                    # Split documents
                    chunks = split_documents(documents)

                    # Create vector database
                    vector_store = create_vector_store(chunks)

                    # Store in session state
                    st.session_state.vector_store = vector_store

                    # Clear previous chat
                    st.session_state.chat_history = []

                st.success(
                    f"Successfully processed {len(uploaded_files)} documents!"
                )

                st.info(
                    f"Total chunks created: {len(chunks)}"
                )

            except Exception as e:

                st.error(f"Error processing documents: {e}")


    # Reset application
    if st.button("Clear Documents & Chat"):

        st.session_state.vector_store = None
        st.session_state.chat_history = []

        st.rerun()


# Main chat interface
st.header("💬 Ask HR Questions")


# Display previous conversations
for message in st.session_state.chat_history:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])

        # Display retrieved source documents
        if message["role"] == "assistant":

            sources = message.get("sources", [])

            if sources:

                with st.expander("View Source Documents"):

                    for index, doc in enumerate(sources):

                        st.write(
                            f"**Source {index + 1}:** "
                            f"{doc.metadata.get('source', 'Unknown')}"
                        )

                        st.write(doc.page_content)


# Chat input
question = st.chat_input(
    "Ask something about HR policies..."
)


if question:

    if st.session_state.vector_store is None:

        st.warning(
            "Please upload and process documents first."
        )

    else:

        # Display user question
        st.session_state.chat_history.append({
            "role": "user",
            "content": question
        })

        with st.chat_message("user"):
            st.write(question)


        # Generate AI response
        with st.chat_message("assistant"):

            with st.spinner("Searching HR documents..."):

                try:

                    answer, retrieved_docs = ask_question(
                        st.session_state.vector_store,
                        question
                    )

                    st.markdown(answer)

                    # Display sources
                    with st.expander("View Source Documents"):

                        for index, doc in enumerate(retrieved_docs):

                            st.write(
                                f"**Source {index + 1}:** "
                                f"{doc.metadata.get('source', 'Unknown')}"
                            )

                            st.write(doc.page_content)

                    # Save assistant response
                    st.session_state.chat_history.append({
                        "role": "assistant",
                        "content": answer,
                        "sources": retrieved_docs
                    })

                except Exception as e:

                    st.error(f"Error generating answer: {e}")
