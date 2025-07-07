from datetime import datetime
from pydantic import BaseModel, UUID1, ConfigDict
from backend.enums import Priority


class Task(BaseModel):
    name: str
    description: str | None
    priority: Priority


class TaskRead(Task):
    model_config = ConfigDict(from_attributes=True)

    id: UUID1
    created_at: datetime
    updated_at: datetime


class TaskUpdate(BaseModel):
    id: UUID1
    name: str | None
    description: str | None
    priority: Priority | None
