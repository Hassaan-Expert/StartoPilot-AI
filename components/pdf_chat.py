import streamlit as st
from langchain_core.messages import AIMessage
from utils.retriever import load_vectorstore
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

def run_pdf_qa():
    st.header("💬 Ask Your PDF")

    if "pdf_path" not in st.session_state:
        st.warning("⚠️ Please upload a PDF first in the 'Upload Business Docs' section.")
        return

    st.markdown(f"**Using file:** `{st.session_state.pdf_path.split('/')[-1]}`")

    # User Question Input
    question = st.text_input("❓ Ask a question based on your uploaded PDF", placeholder="e.g. What is the business model?")

    if question:
        # Load vectorstore retriever
        retriever = load_vectorstore(st.session_state.pdf_path)

        # Prompt and Model
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful assistant. Use the retrieved context to answer the user's question."),
            ("human", "Context:\n{context}\n\nQuestion: {question}")
        ])
        model = ChatGroq(temperature=0.2, model_name="LLaMA3-8b-8192")

        rag_chain = (
            {"context": retriever | RunnablePassthrough(), "question": RunnablePassthrough()}
            | prompt
            | model
            | StrOutputParser()
        )

        with st.spinner("Thinking..."):
            response = rag_chain.invoke(question)

        # Display Answer
        st.markdown("### 💡 Answer:")
        st.write(response)
