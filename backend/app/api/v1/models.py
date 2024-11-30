from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()

# Retrieve available models
LLM_MODELS = settings.LLM_MODELS.split(",")


@router.get("/")
async def get_models():
    """
    Returns the list of available models.
    """
    return {"models": LLM_MODELS}
