from datetime import datetime
from pydantic import BaseModel, UUID1, ConfigDict
from backend.enums import Priority


class Task(BaseModel):
    name: str
    description: str
    priority: Priority


class TaskRead(Task):
    model_config = ConfigDict(from_attributes=True)

    id: UUID1
    created_at: datetime
    updated_at: datetime
