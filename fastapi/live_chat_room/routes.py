from datetime import datetime
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    Cookie,
    Response,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from jose import JWTError
from live_chat_room.schemas import UserSchema
from live_chat_room.db import get_session
from live_chat_room.models import UserModel
from live_chat_room.token import (
    decode_access_token,
    hash_passwd,
    verifiy_passwd,
    gen_access_token,
)
from live_chat_room.ws import WsConnectionManager

router = APIRouter()

ws_manager = WsConnectionManager()


@router.post("/login", tags=["auth"])
def login(user: UserSchema, session: Session = Depends((get_session))) -> JSONResponse:
    avail_user = session.query(UserModel).filter(UserModel.name == user.name).first()
    if not avail_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="authorization error!"
        )

    is_pass_match = verifiy_passwd(passwd=user.password, hash=avail_user.password)
    if not is_pass_match:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="authorization error!"
        )

    token = gen_access_token({"sub": user.name})
    response = JSONResponse(
        {"message": "successfully logged in!", "access_token": token}
    )
    response.set_cookie(key="acc_token", value=token, httponly=True)
    return response


@router.post("/signup", tags=["auth"])
def signup(user: UserSchema, session: Session = Depends((get_session))):
    existing_user = session.query(UserModel).filter(UserModel.name == user.name).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="user already exist!"
        )

    new_user = UserModel(name=user.name, password=hash_passwd(user.password))
    session.add(new_user)
    session.commit()
    return {"message": f"{new_user.name} created successfully!"}


@router.post("/logout", tags=["auth"])
def logout(response: Response):
    response = JSONResponse({"message": "Logged out successfully!"})
    response.delete_cookie("acc_token")
    return response


@router.get("/user/me")
def fetch_current_user(
    acc_token=Cookie(default=None),
    session: Session = Depends((get_session)),
):
    if not acc_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token not avilable"
        )
    try:
        user = decode_access_token(acc_token)

        return {"token user": user}
    except JWTError as e:
        print(f"jwt traceback : {e}")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token not avilable"
        )


@router.websocket("/chat")
async def chat(socket: WebSocket):
    await socket.accept()
    ws_manager.add_connection(socket)
    try:
        while True:
            data = await socket.receive_text()
            await ws_manager.broadcast(
                f"From a client : {data}, at : {datetime.utcnow()}"
            )
    except WebSocketDisconnect as e:
        ws_manager.remove_connection(socket)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="ws connection refused"
        )
