from sqlalchemy import Column, text, String, DateTime, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import expression

from api.database import Base


class Event(Base):
    __tablename__ = "events"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )
    title = Column(String)
    body = Column(String)

    is_active = Column(
        Boolean,
        nullable=False,
        server_default=expression.false()
    )

    date = Column(
        DateTime,
        nullable=False,
        server_default=func.now()
    )
