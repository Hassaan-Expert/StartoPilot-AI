from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

CHROMA_PATH = "data/chroma"

def load_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    return Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_model)

def retrieve_chunks(query, k=5):
    db = load_vectorstore()
    results = db.similarity_search(query, k=k)
    return [doc.page_content for doc in results]

# Optional test run
if __name__ == "__main__":
    sample_query = "What is the value proposition of this business?"
    chunks = retrieve_chunks(sample_query)
    print("📄 Retrieved Chunks:\n")
    for i, chunk in enumerate(chunks, 1):
        print(f"{i}. {chunk}\n")
