from fastapi import APIRouter
from database.db import db

router = APIRouter()

@router.get("/test-db")
async def test_db():
    try:
        await db.command("ping")
        return {
            "database": "connected"
        }
    except Exception as e:
        return {
            "database": "failed",
            "error": str(e)
        }