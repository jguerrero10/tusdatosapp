"""Database session management for SQLModel."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from adapters.database.repositories.event_repository import SQLEventRepository
from adapters.database.session import get_session
from core.entities.event import Event, EventCreate, EventUpdate

router = APIRouter()


@router.post(
    "/",
    response_model=Event,
    description="Create a new event",
    status_code=status.HTTP_201_CREATED,
)
def create_event(event: EventCreate, session: Session = Depends(get_session)):
    """Create a new event."""
    repo = SQLEventRepository(session)
    return repo.create_event(event)


@router.get(
    "/search/",
    response_model=List[Event],
    description="Search events by name",
    status_code=status.HTTP_200_OK,
)
def search_events(name: str, session: Session = Depends(get_session)):
    """Search events by name."""
    repo = SQLEventRepository(session)
    return repo.search_events(name)


@router.get(
    "/",
    response_model=list[Event],
    description="Get all events",
    status_code=status.HTTP_200_OK,
)
def get_events(session: Session = Depends(get_session)):
    """Get all events."""
    repo = SQLEventRepository(session)
    return repo.get_events()


@router.get(
    "/{event_id}",
    response_model=Event,
    description="Get an event",
    status_code=status.HTTP_200_OK,
)
def get_event(event_id: int, session: Session = Depends(get_session)):
    """Get an event by ID."""
    repo = SQLEventRepository(session)
    event = repo.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.patch(
    "/{event_id}",
    response_model=Event,
    description="Update an event",
    status_code=status.HTTP_200_OK,
)
def update_event(event_id: int, event: EventUpdate, session: Session = Depends(get_session)):
    """Update an event by ID."""
    repo = SQLEventRepository(session)
    updated_event = repo.update_event(event_id, event)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event


@router.delete(
    "/{event_id}",
    response_model=Event,
    description="Inactivate an event",
    status_code=status.HTTP_200_OK,
)
def inactivate_event(event_id: int, session: Session = Depends(get_session)):
    """Inactivate an event by ID."""
    repo = SQLEventRepository(session)
    updated_event = repo.inactivate_event(event_id)
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return updated_event
