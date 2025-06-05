from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from live_chat_room.schemas import UserSchema
from live_chat_room.db import get_session
from live_chat_room.models import UserModel
from live_chat_room.token import hash_passwd, verifiy_passwd, gen_access_token

router = APIRouter()


@router.post("/login")
def login(user: UserSchema, session: Session = Depends((get_session))):
    avail_user = session.query(UserModel).filter(UserModel.name == user.name).first()
    if not avail_user:
        print(f"no user found man {avail_user}")
        raise HTTPException(status_code=401, detail="authorization error!")

    is_pass_match = verifiy_passwd(passwd=user.password, hash=avail_user.password)
    if not is_pass_match:
        raise HTTPException(status_code=401, detail="authorization error!")

    token = gen_access_token({"sub": user.name})
    return {"message": "logged in successfull!", "access_token": token}


@router.post("/signup")
def signup(user: UserSchema, session: Session = Depends((get_session))):
    existing_user = session.query(UserModel).filter(UserModel.name == user.name).first()
    if existing_user:
        raise HTTPException(status_code=409, detail="user already exist!")

    new_user = UserModel(name=user.name, password=hash_passwd(user.password))
    session.add(new_user)
    session.commit()
    return {"message": f"{new_user.name} created successfully!"}
