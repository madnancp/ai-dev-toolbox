from datetime import datetime, timedelta
from jose import jwt

SECRET_KEY: str = "wu7j7OhM-xrgssf42SSbikXJEwbV7FbRjBXwrspy2pg"
ALGORITHM: str = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES: int = 2


def get_access_token(data: dict[str, str]) -> str:
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


def decode_token(token: str) -> str:
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])


token = get_access_token({"sub": "john will come for you!"})
print(f"generated token : {token}")

decoded_token = decode_token(token)
print(f"Decoded token : {decoded_token}")

"""
output: 

generated token : eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJqb2huIHdpbGwgY29tZSBmb3IgeW91ISIsImV4cCI6MTc0ODg5MjIwNn0.8kv0u1XNCF7_dBOtOl_q0PX6IzeMt1XNqZjqbb5tVe8

Decoded token : {'sub': 'john will come for you!', 'exp': 1748892206}
"""
