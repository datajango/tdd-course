from fastapi import APIRouter, Depends
from app.config import get_settings, Settings

router = APIRouter()

@router.get("/hello")
async def hello():
    return {"hello": "world"}