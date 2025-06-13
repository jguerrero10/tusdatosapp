"""Database session management for SQLModel."""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from adapters.web.api.auth import router as auth_router
from adapters.web.api.events import router as event_router
from adapters.web.api.speaker import router as speaker_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(event_router, prefix="/api/v1/events", tags=["Events"])

app.include_router(speaker_router, prefix="/api/v1/speakers", tags=["Speakers"])


@app.get("/")
async def root():
    """Root endpoint for the API."""
    return {"message": "Tus Datos, Tu Evento API"}
