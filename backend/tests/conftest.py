import pytest
from fastapi.testclient import TestClient
from app.main import app


@pytest.fixture(scope="module")
def test_client():
    """Fixture to create a FastAPI test client."""
    client = TestClient(app)
    yield client
