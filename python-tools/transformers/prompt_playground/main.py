from fastapi import FastAPI
from prompt_playground.routes import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")
