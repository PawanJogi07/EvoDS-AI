from fastapi import APIRouter
from services.train_service import train_model

router = APIRouter()

@router.post("/train-model")
async def train(target: str):

    return train_model(target)