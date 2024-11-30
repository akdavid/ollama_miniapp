from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from app.services.chat_service import stream_response
from app.core.config import settings

# Initialize the router for the chat
router = APIRouter()


# Model to receive the user message
class ChatRequest(BaseModel):
    prompt: str


@router.post("/")
async def chat_endpoint(request: ChatRequest, model: str):
    """Stream the LLM response with the selected model."""
    # Validate that the model is available
    available_models = settings.LLM_MODELS.split(",")
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
            status_code=500, detail=f"Error during communication with Ollama: {e}"
        )
