# install packages
uv init
uv add streamlit langchain langchain-openai langchain-chroma langchain-text-splitters python-dotenv pypdf python-docx
# run the application

uv run streamlit run app.py

# default url

http://localhost:8501