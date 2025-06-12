"""Database session management for SQLModel."""

from fastapi import FastAPI

from adapters.web.api.events import router as event_router

app = FastAPI()

app.include_router(event_router, prefix="/api/v1/events", tags=["Events"])


@app.get("/")
async def root():
    """Root endpoint for the API."""
    return {"message": "Tus Datos, Tu Evento API"}
