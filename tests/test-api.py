import sys
import os

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)

from backend import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_invalid_model():
    payload = {
        "model_name": "invalid-model",
        "model_provider": "groq",
        "system_prompt": "test",
        "messages": ["hello"],
        "allow_search": False
    }

    response = client.post("/chat", json=payload)

    assert response.status_code == 200
    assert "error" in response.json()