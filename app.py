import streamlit as st
import os
from components import canvas_chat, plan_generator, validator, decision_engine, pdf_chat, upload_files, ai_advisor_chat
from dotenv import load_dotenv

load_dotenv()
st.set_page_config(page_title="StratoPilot – AI Business Copilot", layout="wide")

# === Global Styling & Animations ===
st.markdown("""
    <style>
    .fade-container {
        animation: fadeInSlide 0.9s ease-in-out;
        opacity: 0;
        animation-fill-mode: forwards;
    }
    @keyframes fadeInSlide {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }

    .stButton>button {
        transition: all 0.3s ease-in-out;
        border-radius: 12px;
        font-weight: bold;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    }

    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(249, 197, 78, 0.6);
    }

    h1, h2, h3 {
        color: rgb(39, 124, 160);
    }

    .sidebar .sidebar-content {
        padding: 1rem;
    }

    .sidebar .block-container {
        padding-top: 2rem;
    }

    .hero-title {
        font-size: 3rem;
        font-weight: bold;
        color: rgb(39, 124, 160);
    }

    .tagline {
        font-size: 1.3rem;
        color: rgb(67, 168, 137);
        margin-top: -0.5rem;
    }

    .feature-box {
        background-color: rgba(249, 197, 78, 0.1);
        border-left: 5px solid rgb(249, 197, 78);
        padding: 1rem;
        margin: 1rem 0;
        border-radius: 10px;
    }

    .main > div {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
        padding-left: 3rem !important;
        padding-right: 3rem !important;
    }
    </style>
""", unsafe_allow_html=True)

# === Sidebar Navigation ===
st.sidebar.title("🧭 StratoPilot Copilot")
st.sidebar.markdown("Automate your business strategy with AI 🤖")

page = st.sidebar.radio("📂 Navigate", [
    "🏠 Home",
    "📤 Upload Business Docs",
    "🧠 Canvas Assistant",
    "📑 Auto Plan Generator",
    "💬 PDF Q&A (RAG)",
    "✅ Validate Canvas",
    "🎯 Strategy Suggestions",
    "💬 Ask AI Advisor"
])

# === Page Routing ===
if page == "🏠 Home":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)

    st.markdown("""
        <div class="hero-title">🚀 StratoPilot – Your AI Business Copilot</div>
        <div class="tagline">Build smart business plans, strategies, and insights with zero guesswork.</div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("## 🔍 What You Can Do with StratoPilot:")

    features = [
        ("📤 Upload Documents", "Upload PDFs or Drive link for business data"),
        ("🧠 Canvas Builder", "AI guides you through the Business Model Canvas"),
        ("📑 Plan Generator", "Generate a detailed business plan or pitch deck"),
        ("💬 Ask Your Documents", "AI answers questions from uploaded files using RAG"),
        ("✅ Model Validator", "Get AI-powered feedback and suggestions"),
        ("🎯 Strategic Suggestions", "Let AI recommend smart business actions"),
        ("💬 Ask AI Advisor", "Chat with AI to explore ideas, pivots, improvements")
    ]

    for icon, desc in features:
        st.markdown(f'<div class="feature-box"><b>{icon}</b>: {desc}</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📤 Upload Business Docs":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)
    upload_files.run_upload_files()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🧠 Canvas Assistant":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)
    canvas_chat.run_canvas_chat()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "📑 Auto Plan Generator":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)
    plan_generator.run_plan_generator()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "💬 PDF Q&A (RAG)":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)
    pdf_chat.run_pdf_qa()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "✅ Validate Canvas":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)
    validator.run_validator()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "🎯 Strategy Suggestions":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)
    decision_engine.run_decision_engine()
    st.markdown('</div>', unsafe_allow_html=True)

elif page == "💬 Ask AI Advisor":
    st.markdown('<div class="fade-container">', unsafe_allow_html=True)
    ai_advisor_chat.run_ai_advisor_chat()
    st.markdown('</div>', unsafe_allow_html=True)
