from fastapi import FastAPI
from live_chat_room.routes import router
from live_chat_room.db import Base, engine


Base.metadata.create_all(engine)


app = FastAPI()
app.include_router(router, prefix="/api/v1")
