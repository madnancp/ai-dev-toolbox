from datetime import datetime
from uuid import uuid1
from sqlalchemy import Column, UUID, Enum as SQLEnum, VARCHAR, Text, DATETIME
from backend.core.db import Base
from backend.enums import Priority


class TodoTask(Base):
    __tablename__ = "todotasks"

    id = Column(UUID, default=uuid1, primary_key=True)
    name = Column(VARCHAR(50), nullable=False, unique=False, index=True)
    description = Column(Text, nullable=True, unique=False)
    priority = Column(SQLEnum(Priority), nullable=False, unique=False)
    created_at = Column(DATETIME, default=datetime.now)
    updated_at = Column(DATETIME, default=datetime.now)
