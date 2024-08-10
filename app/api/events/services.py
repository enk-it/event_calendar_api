from typing import Sequence
from datetime import datetime

from sqlalchemy import update, select
from sqlalchemy.ext.asyncio import AsyncSession
from api.events.models import Event
from uuid import UUID


async def create_event(
        db: AsyncSession,
        title: str,
        body: str,
        img: str,
        is_active: bool,
        date: datetime
) -> Event:
    event = Event()
    event.title = title
    event.body = body
    event.img = img
    event.is_active = is_active
    event.date = date.replace(tzinfo=None)
    db.add(event)
    await db.commit()
    return event


async def deactivate_event(
        db: AsyncSession,
        event_id: UUID
):
    query = update(Event).filter_by(id=event_id).values(is_active=False)
    await db.execute(query)
    await db.commit()


async def activate_event(
        db: AsyncSession,
        event_id: UUID
):
    query = update(Event).filter_by(id=event_id).values(is_active=True)
    await db.execute(query)
    await db.commit()


async def get_event_by_id(
        db: AsyncSession,
        event_id: UUID
) -> Event | None:
    query = select(Event).filter_by(id=event_id)
    event = await db.execute(query)
    return event.scalars().first()


async def get_all_events(
        db: AsyncSession,
        active_only: bool = True
) -> Sequence[Event]:
    query = select(Event)

    if active_only:
        query = query.filter_by(is_active=True)

    result = await db.execute(query)
    events = result.scalars().all()
    return events
