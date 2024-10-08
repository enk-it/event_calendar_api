from pydantic import BaseModel
from datetime import datetime
from uuid import UUID


class EventSchema(BaseModel):
    id: UUID
    title: str
    body: str
    img: str | None = None
    date: datetime


class FullEventSchema(EventSchema):
    is_active: bool


class CreateRequest(BaseModel):
    title: str
    body: str
    img: str
    date: datetime
