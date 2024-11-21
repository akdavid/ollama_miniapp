from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
import httpx
import json
import os

router = APIRouter()

# Récupération des variables d'environnement
OLLAMA_API_URL = os.getenv("OLLAMA_API_URL")
LLM_MODEL = os.getenv("LLM_MODEL")


# Modèle pour recevoir le message utilisateur
class ChatRequest(BaseModel):
    prompt: str


async def stream_response(payload: dict):
    """
    Fonction asynchrone pour streamer les réponses de l'API `/api/generate`.
    """
    async with httpx.AsyncClient() as client:
        async with client.stream("POST", OLLAMA_API_URL, json=payload) as response:
            async for line in response.aiter_lines():
                if line.strip():  # Ignore les lignes vides
                    chunk = json.loads(line)
                    if "response" in chunk:
                        yield chunk["response"]


@router.post("/api/chat")
async def chat_endpoint(request: ChatRequest):
    # Utilisation de LLM_MODEL dans la charge utile
    payload = {"model": LLM_MODEL, "prompt": request.prompt}

    try:
        # Retourner une réponse streaming
        return StreamingResponse(stream_response(payload), media_type="text/plain")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur lors de la communication avec Ollama: {e}"
        )
