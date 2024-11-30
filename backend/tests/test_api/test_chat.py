def test_chat_endpoint_invalid_model(test_client):
    """Test an invalid model passed to the /api/v1/chat endpoint."""
    payload = {"prompt": "Hello!", "model": "invalid_model"}
    response = test_client.post("/api/v1/chat?model=invalid_model", json=payload)

    assert response.status_code == 400
    assert "is not available" in response.json()["detail"]
