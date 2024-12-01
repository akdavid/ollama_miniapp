import base64
from io import BytesIO
from PIL import Image
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from app.core.config import settings
from app.core.dependencies import get_openai_client


async def process_image_description(image, prompt):
    """
    Process an image and generate a description using OpenAI's model.

    Args:
        image (UploadFile): The uploaded image file.
        prompt (str): The custom prompt for image description.

    Returns:
        JSONResponse: A response containing the generated description.
    """
    try:
        # Read the image file
        image_data = await image.read()
        print(f"Image received: {image.filename}, size: {len(image_data)} bytes")

        # Open and verify the image
        img = Image.open(BytesIO(image_data))
        img.verify()
        print(f"Image verified: {img.format}, size: {img.size}")

        # Convert image to base64
        img_base64 = base64.b64encode(image_data).decode("utf-8")
        img_url = f"data:{image.content_type};base64,{img_base64}"
        print(f"Base64 Image URL generated (truncated): {img_url[:100]}...")

        # Initialize OpenAI client
        openai_client = get_openai_client()

        # Use the provided custom prompt
        response = openai_client.chat.completions.create(
            model=settings.VLM_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": prompt},
                        {"type": "image_url", "image_url": img_url},
                    ],
                }
            ],
            max_tokens=300,
        )
        print(f"OpenAI API Response: {response}")

        # Extract and return the generated description
        if response.choices and response.choices[0].message:
            description = response.choices[0].message.content.strip()
            print(f"Generated Description: {description}")
            return JSONResponse(content={"description": description})
        else:
            raise HTTPException(
                status_code=500, detail="No valid response generated by OpenAI."
            )

    except Exception as e:
        print(f"Error processing image: {str(e)}")
        raise HTTPException(
            status_code=500, detail=f"Error processing the image : {str(e)}"
        )
