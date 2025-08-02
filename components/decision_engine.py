import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_groq import ChatGroq
from utils.session import get_canvas_data
from utils.prompts import DECISION_ENGINE_PROMPT

def run_decision_engine():
    st.header("🎯 Strategy Suggestions")

    canvas = get_canvas_data()
    if not canvas:
        st.warning("Please complete the Canvas Assistant first.")
        return

    # Show canvas summary
    st.subheader("📋 Canvas Overview")
    for section, content in canvas.items():
        st.markdown(f"**{section}**")
        st.info(content)

    with st.spinner("Analyzing canvas for strategic insights..."):
        prompt = ChatPromptTemplate.from_template(
            DECISION_ENGINE_PROMPT + "\n\nCanvas Data:\n{input}"
        )
        chain: Runnable = prompt | ChatGroq(model="llama3-8b-8192", temperature=0.3)
        full_canvas_text = "\n".join([f"{k}: {v}" for k, v in canvas.items()])
        result = chain.invoke({"input": full_canvas_text})

        st.subheader("🧠 AI Strategy Suggestions")
        st.success(result.content)
