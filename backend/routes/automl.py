from fastapi import APIRouter

from services.automl_service import (
    train_models
)

router = APIRouter()


@router.post("/train-model")
async def train_model(
    target: str
):

    return train_models(
        target
    )