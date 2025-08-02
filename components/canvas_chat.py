import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from utils.prompts import STRATEGY_PROMPT
import time

def run_canvas_chat():
    st.title("🧠 Canvas Assistant")

    if "canvas_data" not in st.session_state:
        st.session_state.canvas_data = {}

    with st.form("canvas_form"):
        st.header("Complete the Business Model Canvas")

        st.session_state.canvas_data["customer_segments"] = st.text_area("Customer Segments")
        st.session_state.canvas_data["value_propositions"] = st.text_area("Value Propositions")
        st.session_state.canvas_data["channels"] = st.text_area("Channels")
        st.session_state.canvas_data["customer_relationships"] = st.text_area("Customer Relationships")
        st.session_state.canvas_data["revenue_streams"] = st.text_area("Revenue Streams")
        st.session_state.canvas_data["key_resources"] = st.text_area("Key Resources")
        st.session_state.canvas_data["key_activities"] = st.text_area("Key Activities")
        st.session_state.canvas_data["key_partnerships"] = st.text_area("Key Partnerships")
        st.session_state.canvas_data["cost_structure"] = st.text_area("Cost Structure")

        submitted = st.form_submit_button("Submit Canvas")

    if submitted:
        st.success("✅ Canvas information saved!")
        time.sleep(1)
        st.rerun()
