from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from live_chat_room.routes import router
from live_chat_room.db import Base, engine

Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router, prefix="/api/v1")
