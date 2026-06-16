# LangGraph-AI-Agent
# LangGraph AI Agent

A multi-provider AI chatbot built with:

* FastAPI (Backend API)
* Streamlit (Frontend UI)
* LangGraph
* LangChain
* Groq Models
* Google Gemini
* Tavily Search

## Features

* Multiple LLM providers

  * Groq
  * Google Gemini
* Web Search using Tavily
* Streamlit User Interface
* FastAPI Backend
* LangGraph ReAct Agent

---

## Project Structure

```text
AI_Asistant/
│
├── ai_agent.py
├── backend.py
├── frontend.py
├── .env
├── requirements.txt
└── README.md
```

---

## Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## Installation

```bash
git clone <repository-url>
conda create -n <env_name> python=3.11
cd AI_Asistant

pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn backend:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Documentation:

```text
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## API Request Example

POST `/chat`

```json
{
  "model_name": "llama-3.3-70b-versatile",
  "model_provider": "groq",
  "system_prompt": "You are a helpful AI assistant.",
  "messages": [
    "What is LangGraph?"
  ],
  "allow_search": true
}
```

Example Response:

```json
{
  "response": "LangGraph is a framework for building stateful AI agents..."
}
```

---

## Supported Models

### Groq

* llama-3.3-70b-versatile
* openai/gpt-oss-120b

### Google

* gemini-2.5-flash

---

# Deploying Backend on Render

## Create Web Service

1. Push project to GitHub.
2. Login to Render.
3. Click New → Web Service.
4. Connect GitHub repository.
5. Configure:

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn backend:app --host 0.0.0.0 --port $PORT
```

---

## Add Environment Variables

In Render Dashboard:

Environment → Add Variables

```text
GROQ_API_KEY=xxxxxxxx
GOOGLE_API_KEY=xxxxxxxx
TAVILY_API_KEY=xxxxxxxx
```

---

## Update Frontend API URL

Replace:

```python
API_URL = "http://127.0.0.1:8000/chat"
```

with:

```python
API_URL = "https://your-render-service.onrender.com/chat"
```

---

## Deploy Streamlit

You can deploy the frontend separately on:

* Render
* Streamlit Community Cloud

If using Streamlit Cloud:

1. Push code to GitHub.
2. Connect repository.
3. Set the main file:

```text
frontend.py
```

4. Deploy.

---

## Author

Pranotosh Mandal
