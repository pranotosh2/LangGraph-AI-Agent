from typing import List
from pydantic import BaseModel
from fastapi import FastAPI
from ai_agent import get_response_from_ai_agent

class RequestState(BaseModel):
    model_name: str
    model_provider: str
    system_prompt: str
    messages: List[str]
    allow_search: bool


ALLOWED_MODEL_NAMES = [
    "openai/gpt-oss-120b",
    "gemini-2.5-flash",
    "llama-3.3-70b-versatile",
    "x-ai/grok-4.1-fast"
]

app = FastAPI(title="LangGraph AI Agent")

# --- ADDED ROOT ENDPOINT FOR RENDER HEALTH CHECKS ---
@app.get("/")
def root_endpoint():
    """
    Root endpoint to confirm service is healthy and running on Render.
    """
    return {
        "status": "healthy",
        "message": "LangGraph AI Backend is running. Access API docs at /docs"
    }

@app.post("/chat")
def chat_endpoint(request: RequestState): 
    """
    API Endpoint to interact with the Chatbot using LangGraph and search tools.
    It dynamically selects the model specified in the request
    """
    if request.model_name not in ALLOWED_MODEL_NAMES:
        return {"error": "Invalid model name. Kindly select a valid AI model"}
    
    llm_id = request.model_name
    query = request.messages
    allow_search = request.allow_search
    system_prompt = request.system_prompt
    provider = request.model_provider

    # Create AI Agent and get response from it! 
    response = get_response_from_ai_agent(llm_id, query, allow_search, system_prompt, provider)
    return response

# Step 3: Run app & Explore Swagger UI Docs
if __name__ == "__main__":
    import uvicorn
    # Changed host to 0.0.0.0 so it accepts external requests if run locally/Dockerized
    uvicorn.run(app, host="0.0.0.0", port=8000)
