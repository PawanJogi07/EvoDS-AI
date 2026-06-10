from fastapi import APIRouter
import joblib
import os

router = APIRouter()

@router.get("/model-info")
async def model_info():

    if not os.path.exists("models/original_features.pkl"):
        return {
            "error": "No trained model found. Please train a model first."
        }

    features = joblib.load(
        "models/original_features.pkl"
    )

    target = joblib.load(
        "models/target_column.pkl"
    )

    return {
        "target": target,
        "features": features
    }