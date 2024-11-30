import httpx
import json
from app.core.logger import logger
from app.core.config import settings


async def stream_response(payload: dict):
    """
    Asynchronous function to stream responses from the `/api/generate` API.
    """
    try:
        async with httpx.AsyncClient() as client:
            async with client.stream(
                "POST", f"{settings.OLLAMA_API_URL}/api/generate", json=payload
            ) as response:
                async for line in response.aiter_lines():
                    if line.strip():  # Ignore empty lines
                        chunk = json.loads(line)
                        if "response" in chunk:
                            yield chunk["response"]
    except Exception as e:
        logger.error(f"Error while streaming response: {e}")
        raise
