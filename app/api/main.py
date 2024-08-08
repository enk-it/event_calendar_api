from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.events.routers import router as events_router

app = FastAPI(
    title="Fitness API",
    docs_url="/api/v1/docs",
    redoc_url="/api/v1/redoc",
)


origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(events_router)

