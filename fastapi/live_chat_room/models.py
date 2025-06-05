from sqlalchemy import Column, Integer, String
from live_chat_room.db import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    password = Column(String)
