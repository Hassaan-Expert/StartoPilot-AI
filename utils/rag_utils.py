import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores.base import VectorStoreRetriever
from langchain_core.documents import Document

CHROMA_PATH = "data/chroma_store"

def extract_text_from_pdf(pdf_path):
    text = ""
    doc = fitz.open(pdf_path)
    for page in doc:
        text += page.get_text()
    return text

def chunk_text(text, chunk_size=800, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ".", "!", "?", ",", " ", ""]
    )
    chunks = splitter.create_documents([text])
    return chunks

def store_chunks_in_chroma(chunks, persist_path=CHROMA_PATH):
    os.makedirs(persist_path, exist_ok=True)
    embeddings = OpenAIEmbeddings()  # Replace with Groq later
    db = Chroma.from_documents(chunks, embedding=embeddings, persist_directory=persist_path)
    db.persist()
    return db

def load_existing_chroma(persist_path=CHROMA_PATH):
    embeddings = OpenAIEmbeddings()
    db = Chroma(persist_directory=persist_path, embedding_function=embeddings)
    return db

def process_pdf_for_rag(pdf_file_path):
    text = extract_text_from_pdf(pdf_file_path)
    chunks = chunk_text(text)
    db = store_chunks_in_chroma(chunks)
    return db
