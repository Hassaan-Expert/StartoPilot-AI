import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_groq import ChatGroq
from utils.session import get_canvas_data
from utils.prompts import VALIDATOR_PROMPT

def run_validator():
    st.header("✅ Validate Your Canvas")

    canvas = get_canvas_data()
    if not canvas:
        st.warning("Please complete the Canvas Assistant first.")
        return

    # Display user input for reference
    st.subheader("🧾 Your Canvas Summary")
    for section, content in canvas.items():
        st.markdown(f"**{section}**")
        st.info(content)

    with st.spinner("Analyzing your canvas..."):
        # Prompt and chain setup
        prompt = ChatPromptTemplate.from_template(
            VALIDATOR_PROMPT + "\n\nCanvas Data:\n{input}"
        )

        chain: Runnable = prompt | ChatGroq(model="llama3-8b-8192", temperature=0.3)
        full_canvas_text = "\n".join([f"{k}: {v}" for k, v in canvas.items()])
        validation_result = chain.invoke({"input": full_canvas_text})

        st.subheader("📊 Validation Result")
        st.success(validation_result.content)
