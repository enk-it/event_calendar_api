from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.auth.dependencies import get_current_auth_user
from api.database import get_session
from api.events.exceptions import WrongEventId
from api.events.schemas import EventSchema, CreateRequest, FullEventSchema
from api.events import services as event_services

router = APIRouter(prefix="/api/v1/events", tags=["events"])


@router.get("/", response_model=list[EventSchema])
async def get_active_events(
        session: AsyncSession = Depends(get_session),
):
    events = await event_services.get_all_events(session)
    return events


@router.get("/all", response_model=list[FullEventSchema])
async def get_all_events(
        session: AsyncSession = Depends(get_session),
        auth=Depends(get_current_auth_user),
):
    events = await event_services.get_all_events(session, active_only=False)
    return events


@router.post("/create", response_model=EventSchema)
async def create_event(
        create_request: CreateRequest,
        session: AsyncSession = Depends(get_session),
        auth=Depends(get_current_auth_user),
):
    event = await event_services.create_event(
        session,
        create_request.title,
        create_request.body,
        create_request.img,
        False,
        create_request.date,
    )

    return event


@router.patch("/activate/{event_id}", response_model=EventSchema)
async def activate_event(
        event_id: UUID,
        session: AsyncSession = Depends(get_session),
        auth=Depends(get_current_auth_user),

):
    event = await event_services.get_event_by_id(
        session,
        event_id
    )
    if event is None:
        raise WrongEventId
    await event_services.activate_event(
        session,
        event_id
    )
    return event


@router.patch("/deactivate/{event_id}", response_model=EventSchema)
async def deactivate_event(
        event_id: UUID,
        session: AsyncSession = Depends(get_session),
        auth=Depends(get_current_auth_user),
):
    event = await event_services.get_event_by_id(
        session,
        event_id
    )
    if event is None:
        raise WrongEventId
    await event_services.deactivate_event(
        session,
        event_id
    )
    return event
