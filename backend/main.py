# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat import router as chat_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow React to call this API
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "✅ FastAPI is running"}
