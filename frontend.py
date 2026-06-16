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

MODEL_NAMES_GROQ = [
    "llama-3.3-70b-versatile",
    "openai/gpt-oss-120b"
]

MODEL_NAMES_GOOGLE = [
    "gemini-2.5-flash"
]

provider = st.radio(
    "Select Provider",
    ("groq", "google")
)

if provider == "groq":
    selected_model = st.selectbox(
        "Select Model",
        MODEL_NAMES_GROQ
    )
else:
    selected_model = st.selectbox(
        "Select Model",
        MODEL_NAMES_GOOGLE
    )

allow_web_search = st.checkbox(
    "Allow Web Search"
)

user_query = st.text_area(
    "Enter Query",
    height=150
)



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

    # 1. Handle network connection strictly
    try:
        response = requests.post(
            API_URL,
            json=payload,
            timeout=120
        )
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to connect to API backend server: {str(e)}")
        st.stop()

    # 2. Process the server response safely
    if response.status_code == 200:
        try:
            data = response.json()
            
            # Ensure the response data is a dictionary before looking up string keys
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
                # Fallback if JSON parsed into a plain string or list instead of a dict
                st.subheader("Response")
                st.write(data)
                
        except ValueError:
            # Falls here if the backend returned a 200 OK but sent raw text instead of JSON
            st.subheader("Response (Raw Text)")
            st.write(response.text)

    else:
        # Displays explicit error codes (like 404, 422 Unprocessable Entity, or 500 Internal Error)
        st.error(f"Backend Error (Status {response.status_code}): {response.text}")
