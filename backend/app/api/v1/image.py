from fastapi import APIRouter, UploadFile, File
from app.services.image_service import process_image_description

router = APIRouter()


@router.post("/")
async def image_description(image: UploadFile = File(...)):
    """
    Route to process an image and generate a description.
    """
    return await process_image_description(image)
