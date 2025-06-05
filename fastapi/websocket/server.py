from datetime import datetime
from pydantic import BaseModel
from fastapi import HTTPException, WebSocket, FastAPI, Request, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


class MessageSchema(BaseModel):
    title: str
    content: str


template = Jinja2Templates("templates")

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def index(request: Request) -> HTMLResponse:
    return template.TemplateResponse(name="index.html", request=request)


@app.websocket("/ws")
async def live_chat(socket: WebSocket):
    await socket.accept()
    try:
        while True:
            data = await socket.receive_text()
            await socket.send_text(f"echo : {data} , receved at : {datetime.utcnow()}")

    except WebSocketDisconnect:
        raise HTTPException(status_code=404, detail="connection refused")
