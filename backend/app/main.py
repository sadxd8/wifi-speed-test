from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import speed_test

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Include the speed test router
app.include_router(speed_test.router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Internet Speed Test API!"}