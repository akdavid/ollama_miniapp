import os


class Settings:
    # Main configuration
    APP_NAME: str = "Ollama MiniApp"
    API_V1_PREFIX: str = "/api/v1"

    # Environment variables
    OLLAMA_API_URL: str = os.getenv("OLLAMA_API_URL", "http://localhost:11434")
    OLLAMA_API_KEY: str = os.getenv("OLLAMA_API_KEY", "ollama")
    LLM_MODELS: str = os.getenv("LLM_MODELS", "model1,model2")
    VLM_MODEL: str = os.getenv("VLM_MODEL", "vlm_model")
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")


# Singleton instance of settings
settings = Settings()
