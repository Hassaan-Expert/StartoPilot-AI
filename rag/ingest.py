import os
import fitz  # PyMuPDF
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

CHROMA_PATH = "data/chroma"
DOCS_PATH = "data/user_docs"

def extract_text_from_pdfs(folder_path):
    all_text = ""
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            file_path = os.path.join(folder_path, filename)
            doc = fitz.open(file_path)
            for page in doc:
                all_text += page.get_text()
            doc.close()
    return all_text

def chunk_text(text, chunk_size=500, chunk_overlap=100):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return splitter.create_documents([text])

def embed_and_store(chunks):
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(documents=chunks, embedding=embedding_model, persist_directory=CHROMA_PATH)
    db.persist()
    print("✅ Embeddings stored successfully in ChromaDB.")

def run_ingest_pipeline():
    print("📥 Extracting text from PDFs...")
    raw_text = extract_text_from_pdfs(DOCS_PATH)

    print("✂️ Splitting into chunks...")
    chunks = chunk_text(raw_text)

    print(f"🧠 Total chunks created: {len(chunks)}")
    print("🔗 Embedding & saving into Chroma...")
    embed_and_store(chunks)

if __name__ == "__main__":
    run_ingest_pipeline()
