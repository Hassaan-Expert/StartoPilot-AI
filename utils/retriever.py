import os
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.vectorstores import VectorStoreRetriever

def load_vectorstore(pdf_path: str) -> VectorStoreRetriever:
    # Ensure Chroma store directory exists
    folder_path = "chroma_store"
    os.makedirs(folder_path, exist_ok=True)

    # Use a local embedding model (no API key needed)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    # Initialize Chroma without deprecated Settings
    vectordb = Chroma(
        persist_directory=folder_path,
        embedding_function=embeddings
    )

    # Return retriever
    return vectordb.as_retriever()
