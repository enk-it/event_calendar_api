import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.database import get_session
from api.events.schemas import EventSchema

router = APIRouter(prefix="/api/v1/events", tags=["users"])


@router.get("/events", response_model=list[EventSchema])
async def update_avatar(
        session: AsyncSession = Depends(get_session),
):
    return [
        {
            "id": "ae39bedc-3cd4-4e7d-b765-80949eaa16cd",
            "title": "aasdas",
            "body": "adsaas",
            "date": datetime.datetime.now()
        }
    ]
