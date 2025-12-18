from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.services.model import model_service

router = APIRouter()


class AnalysisRequest(BaseModel):
    filename: str
    content_type: Optional[str] = "image/jpeg"
    metadata: Optional[dict] = {}


class AnalysisResponse(BaseModel):
    filename: str
    is_deepfake: bool
    confidence: float
    model_version: str
    message: str


@router.post("/analysis/deepfake", response_model=AnalysisResponse)
async def analyze_media(request: AnalysisRequest):
    """
    Analyzes the provided media file for deepfake content.
    """
    if not request.filename:
        raise HTTPException(status_code=400, detail="Filename is required")

    # Call the mock model service
    result = model_service.predict(request)

    message = (
        "Deepfake detected." if result["is_deepfake"] else "Media appears authentic."
    )

    return AnalysisResponse(
        filename=request.filename,
        is_deepfake=result["is_deepfake"],
        confidence=result["confidence"],
        model_version=result["model_version"],
        message=message,
    )
