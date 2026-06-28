from dotenv import load_dotenv
from pathlib import Path
import os
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage , HumanMessage

env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

import streamlit as st


# Model
model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0.9
)

st.title("AI Chatbot")

# Mode selection
mode_option = st.selectbox(
    "Choose your AI mode",
    ["Angry mode", "Funny mode", "Sad mode"]
)

if mode_option == "Angry mode":
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_option == "Funny mode":
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif mode_option == "Sad mode":
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."

# Initialize messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]

# Reset conversation if mode changes
if "current_mode" not in st.session_state:
    st.session_state.current_mode = mode

if st.session_state.current_mode != mode:
    st.session_state.messages = [
        SystemMessage(content=mode)
    ]
    st.session_state.current_mode = mode

# Display previous chat
for message in st.session_state.messages:
    if isinstance(message, HumanMessage):
        with st.chat_message("user"):
            st.write(message.content)
    elif isinstance(message, AIMessage):
        with st.chat_message("assistant"):
            st.write(message.content)

# Chat input
prompt = st.chat_input("Type your message")

if prompt:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("user"):
        st.write(prompt)

    # Generate response
    response = model.invoke(st.session_state.messages)

    # Add AI response
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.write(response.content)