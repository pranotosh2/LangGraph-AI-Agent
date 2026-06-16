# 🤖 LangGraph AI Agent

A production-ready AI chatbot built using LangGraph, LangChain, FastAPI, Streamlit, Groq, Gemini, and Tavily Search.

## 🚀 Live Demo

[https://langgraph-ai-frontend.onrender.com](https://langgraph-ai-frontend.onrender.com/)

---

## 📌 Features

* Multi-Provider LLM Support

  * Groq Models
  * Google Gemini
* LangGraph ReAct Agent
* Optional Web Search via Tavily
* FastAPI REST API
* Streamlit Frontend
* Environment Variable Management
* Render Deployment
* GitHub Actions CI/CD
* Automated Testing with Pytest

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Streamlit Frontend
 │
 ▼
FastAPI Backend
 │
 ▼
LangGraph ReAct Agent
 │
 ├── Groq
 │
 ├── Gemini
 │
 └── Tavily Search
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* Uvicorn

### AI Framework

* LangChain
* LangGraph

### LLM Providers

* Groq
* Google Gemini

### Search Tool

* Tavily Search

### DevOps

* GitHub Actions
* Render

### Testing

* Pytest

---

## 📂 Project Structure

```text
AI_Asistant/
│
├── ai_agent.py
├── backend.py
├── frontend.py
│
├── tests/
│   └── test_api.py
│
├── .github/
│   └── workflows/
│       └── ci_cd.yml
│
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
GOOGLE_API_KEY=your_google_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## 🔧 Installation

```bash
git clone https://github.com/pranotosh2/LangGraph-AI-Agent.git

cd LangGraph-AI-Agent

conda create -n ai python=3.11

conda activate ai

pip install -r requirements.txt
```

---

## ▶️ Run Backend

```bash
uvicorn backend:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

## ▶️ Run Frontend

```bash
streamlit run frontend.py
```

Frontend URL:

```text
http://localhost:8501
```

---
---

## 🤖 Supported Models

### Groq

* llama-3.3-70b-versatile
* openai/gpt-oss-120b

### Google

* gemini-2.5-flash

---

## 🧪 Running Tests

Run all tests:

```bash
pytest -v
```

Example Output:

```text
tests/test_api.py::test_invalid_model PASSED
```

---

## 🚀 Deployment

### Backend (Render)

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn backend:app --host 0.0.0.0 --port $PORT
```

Environment Variables:

```env
GROQ_API_KEY=
GOOGLE_API_KEY=
TAVILY_API_KEY=
```

---

### Frontend (Render)

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
streamlit run frontend.py --server.port=$PORT --server.address=0.0.0.0
```

Environment Variable:

```env
BACKEND_URL=https://langgraph-ai-backend.onrender.com/chat
```
---

## 🔄 CI/CD Pipeline

```text
Developer Push
       │
       ▼
GitHub Repository
       │
       ▼
GitHub Actions
       │
       ├── Install Dependencies
       ├── Run Pytest
       └── Deploy to Render
```
---

## 👨‍💻 Author

Pranotosh Mandal

GitHub:
https://github.com/pranotosh2

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
