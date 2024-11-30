from fastapi import APIRouter
from .chat import router as chat_router
from .image import router as image_router
from .models import router as models_router

# Main router for version 1
router = APIRouter()

# Include sub-routers
router.include_router(chat_router, prefix="/chat", tags=["chat"])
router.include_router(image_router, prefix="/image-description", tags=["image"])
router.include_router(models_router, prefix="/models", tags=["models"])


@router.get("/test")
async def test_endpoint():
    """Simple endpoint to test backend communication."""
    return {"message": "Backend communication successful!"}
