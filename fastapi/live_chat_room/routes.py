from fastapi import APIRouter, Depends, HTTPException, status, Cookie, Response
from fastapi.responses import JSONResponse
from sqlalchemy import JSON
from sqlalchemy.orm import Session
from live_chat_room.schemas import UserSchema
from live_chat_room.db import get_session
from live_chat_room.models import UserModel
from live_chat_room.token import hash_passwd, verifiy_passwd, gen_access_token

router = APIRouter()


@router.post("/login")
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


@router.post("/signup")
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


@router.post("/logout")
def logout(response: Response):
    response = JSONResponse({"message": "Logged out successfully!"})
    response.delete_cookie("acc_token")
    return response


@router.get("/show")
def get_token(acc_token=Cookie(default=None)):
    if not acc_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="token not avilable"
        )
    return {"token": acc_token}
