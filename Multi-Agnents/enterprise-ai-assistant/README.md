# restore the packages
uv sync
# Run the document ingestion

uv run python ingest.py

# start the Streamlit application

uv run streamlit run app.py