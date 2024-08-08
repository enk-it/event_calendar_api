from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class EventSchema(BaseModel):
    id: UUID
    title: str
    body: str
    date: datetime
