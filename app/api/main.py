from fastapi import FastAPI

from api.events.routers import router as events_router

app = FastAPI(
    title="Fitness API",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)

app.include_router(events_router)

