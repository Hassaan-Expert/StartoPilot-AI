import streamlit as st

def get_canvas_data():
    return st.session_state.get("canvas_data", {})

def save_canvas_data(canvas_data):
    st.session_state["canvas_data"] = canvas_data
