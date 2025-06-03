from jose import JWTError
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from jwt.token import (
    generate_access_token,
    decode_token,
    hash_password,
    verify_password,
)

dummy_data: dict[str, str] = {}


class UserSchema(BaseModel):
    name: str
    password: str


app = FastAPI()


@app.post("/signup")
def signup(user: UserSchema):

    if user.name in dummy_data.keys():
        raise HTTPException(status_code=409, detail="User is already exists")

    hashed_pass = hash_password(user.password)
    dummy_data[user.name] = hashed_pass
    return {"db": dummy_data}


@app.post("/login")
def login(user: UserSchema):

    if user.name not in dummy_data.keys():
        raise HTTPException(status_code=401, detail="un authorized")

    user_hash_pass = dummy_data.get(user.name)
    is_password_valid = verify_password(passwd=user.password, hash=user_hash_pass)

    if not is_password_valid:
        raise HTTPException(status_code=401, detail="un authorized")

    access_token = generate_access_token({"sub": user.name})

    return {"access_token": access_token}


@app.get("/protected")
def secret_path(token: str):
    try:
        data = decode_token(token=token)
        user = data["sub"]
        if user not in dummy_data.keys():
            raise HTTPException(status_code=401, detail="Invalid token")
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

    return {"Yes you can permission to view this": "hurray"}
