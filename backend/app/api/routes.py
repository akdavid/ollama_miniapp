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
async def chat_endpoint(request: ChatRequest, model: str):
    """Stream the LLM response with the selected model."""
    # Vérifiez que le modèle est valide
    available_models = os.getenv("LLM_MODELS", "").split(",")
    if model not in available_models:
        raise HTTPException(
            status_code=400,
            detail=f"Model '{model}' is not available. Choose from {available_models}.",
        )

    payload = {"model": model, "prompt": request.prompt}

    try:
        return StreamingResponse(stream_response(payload), media_type="text/plain")
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Erreur lors de la communication avec Ollama: {e}"
        )


@router.get("/api/models")
async def get_models():
    """Retourne la liste des modèles disponibles."""
    models = os.getenv("LLM_MODELS", "").split(",")
    return {"models": models}
