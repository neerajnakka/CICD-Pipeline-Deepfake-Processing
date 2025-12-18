from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    """
    Test the health check endpoint.
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_analyze_deepfake_valid_request():
    """
    Test the deepfake analysis endpoint with a valid payload.
    """
    payload = {
        "filename": "suspicious_video.mp4",
        "content_type": "video/mp4"
    }
    response = client.post("/v1/analysis/deepfake", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["filename"] == "suspicious_video.mp4"
    assert "is_deepfake" in data
    assert "message" in data

def test_analyze_deepfake_missing_filename():
    """
    Test validation error when filename is missing.
    """
    payload = {
        "content_type": "video/mp4"
    }
    # Pydantic validation should catch this (422 Unprocessable Entity)
    response = client.post("/v1/analysis/deepfake", json=payload)
    assert response.status_code == 422
