import random
from typing import Dict, Any

class DeepfakeModel:
    """
    A mock model service that simulates deepfake detection.
    In a real scenario, this would load a PyTorch/TensorFlow model.
    """
    
    def __init__(self):
        # Simulate loading heavy weights
        pass

    def predict(self, input_data: Any) -> Dict[str, Any]:
        """
        Simulates inference latency and returns a mock prediction.
        """
        # Logic: Randomly assign a confidence score
        confidence = random.uniform(0.60, 0.99)
        is_deepfake = random.choice([True, False])
        
        # Make it slightly deterministic for consistency in demos if needed, 
        # but for now random is fine to show variety.
        
        return {
            "is_deepfake": is_deepfake,
            "confidence": round(confidence, 4),
            "model_version": "v1.0.0-mock",
            "processing_time_ms": random.randint(50, 200)
        }

model_service = DeepfakeModel()
