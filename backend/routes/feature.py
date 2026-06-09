from fastapi import APIRouter

from services.feature_service import (
    feature_importance
)

router = APIRouter()

@router.get("/feature-importance")
async def importance():

    return feature_importance()