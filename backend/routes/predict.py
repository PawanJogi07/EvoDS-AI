from fastapi import APIRouter

from services.predict_service import (
    predict
)

router = APIRouter()


@router.post("/predict")
async def predict_route(
    data: dict
):

    return predict(data)