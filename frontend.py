import streamlit as st
import requests
import os

st.set_page_config(
    page_title="LangGraph Agent",
    layout="centered"
)

st.title("🤖 AI Chatbot Agent")

system_prompt = st.text_area(
    "System Prompt",
    value="You are a helpful AI assistant."
)

# 1. Aligned exactly with ALLOWED_MODEL_NAMES in backend.py
MODEL_MAP = {
    "groq": ["llama-3.3-70b-versatile"],
    "google": ["gemini-2.5-flash"],
    "openai": ["openai/gpt-oss-120b"],
    "x-ai": ["x-ai/grok-4.1-fast"]
}

# Dynamic radio selection using keys from our model map
provider = st.radio(
    "Select Provider",
    options=list(MODEL_MAP.keys())
)

# Dynamically populate the dropdown based on selected provider
selected_model = st.selectbox(
    "Select Model",
    options=MODEL_MAP[provider]
)

allow_web_search = st.checkbox(
    "Allow Web Search"
)

user_query = st.text_area(
    "Enter Query",
    height=150
)

# Pulled from your Render environment variable setup
API_URL = os.getenv(
    "BACKEND_URL",
    "https://langgraph-ai-backend.onrender.com/chat"
)

if st.button("Ask Agent"):

    if not user_query.strip():
        st.warning("Please enter a query.")
        st.stop()

    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    # Handle network connection strictly
    try:
        response = requests.post(
            API_URL,
            json=payload,
            timeout=120
        )
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to API backend server: {str(e)}")
        st.stop()

    # Process the server response safely
    if response.status_code == 200:
        try:
            data = response.json()
            
            if isinstance(data, dict):
                if "error" in data:
                    st.error(data["error"])
                elif "response" in data:
                    st.subheader("Response")
                    st.write(data["response"])
                else:
                    st.warning("Unexpected JSON structure received from API.")
                    st.json(data)
            else:
                st.subheader("Response")
                st.write(data)
                
        except ValueError:
            st.subheader("Response (Raw Text)")
            st.write(response.text)

    else:
        st.error(f"Backend Error (Status {response.status_code}): {response.text}")
