import os
import shutil
from fastapi import APIRouter, HTTPException, File, Depends

router = APIRouter()

@router.get("/hello")
async def hello():
    return { "message" : "Hello World"}