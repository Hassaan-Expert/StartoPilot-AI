import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_groq import ChatGroq
from utils.session import get_canvas_data
from utils.prompts import STRATEGY_PROMPT
from utils.helpers import generate_pdf

def run_plan_generator():
    st.header("📑 Auto Plan Generator")

    canvas = get_canvas_data()
    if not canvas:
        st.warning("Please complete the Canvas Assistant first.")
        return

    # Display Canvas Summary
    st.subheader("🧾 Your Canvas Summary")
    for section, content in canvas.items():
        st.markdown(f"**{section}**")
        st.info(content)

    with st.spinner("Generating business plan..."):
        prompt = ChatPromptTemplate.from_template(
            STRATEGY_PROMPT + "\n\nCanvas Data:\n{input}"
        )
        chain: Runnable = prompt | ChatGroq(model="llama3-8b-8192", temperature=0.4)
        full_canvas_text = "\n".join([f"{k}: {v}" for k, v in canvas.items()])
        result = chain.invoke({"input": full_canvas_text})

        st.subheader("📄 Generated Business Plan")
        st.success(result.content)

        # Allow download
        pdf_path = generate_pdf(result.content , content)
        with open(pdf_path, "rb") as f:
            st.download_button("📥 Download as PDF", f, file_name="Business_Plan.pdf")
    