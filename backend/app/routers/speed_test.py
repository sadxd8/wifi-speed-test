import asyncio
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/download")
async def download_test():
    # Generate a fake file of 50MB
    data = b"0" * 50 * 1024 * 1024  # 50MB
    return data

@router.post("/upload")
async def upload_test(file: bytes):
    # Here you would normally measure the received file size to determine upload speed
    return {"message": "Upload succeeded!"}

@router.get("/ping")
async def ping_test():
    return {"latency": "Ping response successful!"}
