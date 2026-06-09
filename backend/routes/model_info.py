from fastapi import APIRouter
import joblib

router = APIRouter()


@router.get("/model-info")
async def model_info():

    columns = joblib.load(
        "models/original_features.pkl"
    )

    target = joblib.load(
        "models/target_column.pkl"
    )

    return {
        "target": target,
        "features": columns
    }