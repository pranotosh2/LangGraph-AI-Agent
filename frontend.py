import streamlit as st
import requests
import os

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="LangGraph AI Agent",
    layout="centered"
)

st.title("🤖 AI Chatbot Agent")

# --------------------------------------------------
# System Prompt
# --------------------------------------------------
system_prompt = st.text_area(
    "System Prompt",
    value="You are a helpful AI assistant."
)

# --------------------------------------------------
# Models
# --------------------------------------------------
MODEL_MAP = {
    "groq": [
        "llama-3.3-70b-versatile",
        "openai/gpt-oss-120b"
    ],
    "google": [
        "gemini-2.5-flash"
    ]
}

# --------------------------------------------------
# Provider Selection
# --------------------------------------------------
provider = st.radio(
    "Select Provider",
    options=list(MODEL_MAP.keys())
)

# --------------------------------------------------
# Model Selection
# --------------------------------------------------
selected_model = st.selectbox(
    "Select Model",
    options=MODEL_MAP[provider]
)

# --------------------------------------------------
# Search Option
# --------------------------------------------------
allow_web_search = st.checkbox(
    "Allow Web Search"
)

# --------------------------------------------------
# User Query
# --------------------------------------------------
user_query = st.text_area(
    "Enter Query",
    height=150
)

# --------------------------------------------------
# Backend URL
# --------------------------------------------------
API_URL = os.getenv(
    "BACKEND_URL",
    "https://langgraph-ai-backend.onrender.com/chat"
)

# --------------------------------------------------
# Submit Button
# --------------------------------------------------
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

    try:
        with st.spinner("Generating response..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=120
            )

    except requests.exceptions.RequestException as e:
        st.error(
            f"Failed to connect to backend server:\n{str(e)}"
        )
        st.stop()

    # --------------------------------------------------
    # Response Handling
    # --------------------------------------------------
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
                    st.subheader("Response")
                    st.json(data)

            else:
                st.subheader("Response")
                st.write(data)

        except ValueError:
            st.subheader("Response")
            st.write(response.text)

    else:
        st.error(
            f"Backend Error ({response.status_code})\n{response.text}"
        )
