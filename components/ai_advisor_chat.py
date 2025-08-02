import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.runnables import RunnableConfig
import os

def run_ai_advisor_chat():
    st.title("💬 Ask the AI Business Advisor")
    st.markdown("Use this assistant to ask any business-related question like:")
    st.markdown("- “What’s the best revenue stream for a subscription product?”")
    st.markdown("- “How should I target students for my app?”")
    st.markdown("- “What happens if I switch to a Premium model?”")
    st.markdown("---")

    if "advisor_chat_history" not in st.session_state:
        st.session_state.advisor_chat_history = [
            AIMessage(content="👋 Hi! I'm your AI Business Advisor. Ask me anything about your startup, model, or idea.")
        ]

    # Display chat history
    for msg in st.session_state.advisor_chat_history:
        if isinstance(msg, HumanMessage):
            with st.chat_message("user"):
                st.markdown(msg.content)
        elif isinstance(msg, AIMessage):
            with st.chat_message("assistant"):
                st.markdown(msg.content)

    # User prompt input
    user_input = st.chat_input("Ask a business question...")
    if user_input:
        st.session_state.advisor_chat_history.append(HumanMessage(content=user_input))

        # AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                llm = ChatGroq(temperature=0.7, model_name="LLaMA3-70b-8192")
                prompt = ChatPromptTemplate.from_messages([
                    ("system", "You are a helpful and strategic business advisor. Answer clearly and practically."),
                    ("human", "{question}")
                ])
                chain = prompt | llm
                response = chain.invoke({"question": user_input}, config=RunnableConfig())
                st.session_state.advisor_chat_history.append(AIMessage(content=response.content))
                st.markdown(response.content)
