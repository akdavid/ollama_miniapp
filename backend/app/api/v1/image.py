from fastapi import APIRouter, UploadFile, File, Form
from app.services.image_service import process_image_description

router = APIRouter()


@router.post("/")
async def image_description(
    image: UploadFile = File(...), prompt: str = Form("What's in this image?")
):
    """
    Endpoint to process an image and generate a description.
    """
    return await process_image_description(image, prompt)
