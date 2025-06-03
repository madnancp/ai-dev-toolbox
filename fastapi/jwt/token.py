from datetime import datetime, timedelta
from secrets import token_urlsafe
from passlib.context import CryptContext
from jose import jwt


ACCESS_TOKEN_EXPIRE_MINUTES: int = 2
ALGORITHM: str = "HS256"
SECRET_KEY = token_urlsafe(32)

pass_crypt = CryptContext(schemes=["bcrypt"])


def hash_password(passwd: str) -> str:
    return pass_crypt.hash(passwd)


def verify_password(passwd: str, hash: str) -> bool:
    return pass_crypt.verify(secret=passwd, hash=hash)


def generate_access_token(data: dict) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> dict:
    return jwt.decode(token=token, algorithms=[ALGORITHM], key=SECRET_KEY)
