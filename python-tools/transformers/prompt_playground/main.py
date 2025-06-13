from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prompt_playground.routes import router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(router, prefix="/api/v1")
