from openai import OpenAI
from app.core.config import settings


def get_openai_client():
    """Configure and return an OpenAI client."""
    return OpenAI(
        base_url=f"{settings.OLLAMA_API_URL}/v1/",
        api_key=settings.OLLAMA_API_KEY,
    )
