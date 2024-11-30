def test_image_description_invalid_file(test_client):
    """Test a non-image file sent to /api/v1/image-description."""
    invalid_file = {"image": ("test.txt", "This is not an image.", "text/plain")}

    response = test_client.post("/api/v1/image-description", files=invalid_file)

    assert response.status_code == 500
    assert "Error processing the image" in response.json()["detail"]
