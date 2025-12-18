from app.services.model import model_service


def test_predict_structure():
    """
    Test that the prediction returns the correct structure and data types.
    """
    mock_input = {"filename": "test.jpg"}
    result = model_service.predict(mock_input)

    assert "is_deepfake" in result
    assert isinstance(result["is_deepfake"], bool)

    assert "confidence" in result
    assert isinstance(result["confidence"], float)

    assert "model_version" in result
    assert isinstance(result["model_version"], str)


def test_confidence_range():
    """
    Test that confidence score is within expected bounds (0.0 to 1.0).
    """
    mock_input = {"filename": "test.jpg"}
    result = model_service.predict(mock_input)
    confidence = result["confidence"]

    assert 0.0 <= confidence <= 1.0
