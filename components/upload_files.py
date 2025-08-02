import streamlit as st
import os

def run_upload_files():
    st.title("📤 Upload Business Documents")
    uploaded_file = st.file_uploader("Upload your business PDF", type=["pdf"])

    if uploaded_file:
        save_path = os.path.join("user_docs", uploaded_file.name)
        os.makedirs("user_docs", exist_ok=True)

        with open(save_path, "wb") as f:
            f.write(uploaded_file.read())

        st.session_state.pdf_path = save_path  # ✅ Save for use in Q&A
        st.success("✅ File uploaded and ready to use in PDF Q&A.")
