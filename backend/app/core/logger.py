import logging


def setup_logger():
    """Configure and return the logger."""
    logger = logging.getLogger("ollama_miniapp")
    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)  # Peut être ajusté avec `settings.LOG_LEVEL`
    return logger


# Instance globale du logger
logger = setup_logger()
