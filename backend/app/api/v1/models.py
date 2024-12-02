from fastapi import APIRouter
from app.core.config import settings

router = APIRouter()


@router.get("/")
async def get_models():
    """
    Returns the list of available models, including LLM and VLM.
    """
    LLM_MODELS = settings.LLM_MODELS.split(",")
    VLM_MODEL = settings.VLM_MODEL
    return {
        "llm_models": LLM_MODELS,
        "vlm_model": VLM_MODEL,
    }
