"""Database session management for SQLModel."""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from adapters.database.repositories.event_repository import SQLEventRepository
from adapters.database.repositories.registration_repository import SQLRegistrationRepository
from adapters.database.session import get_session
from core.entities.event import Event, EventCreate, EventUpdate
from core.entities.user import User
from core.security.dependencies import get_current_user

router = APIRouter()


@router.post(
    "/",
    response_model=Event,
    description="Create a new event",
    status_code=status.HTTP_201_CREATED,
)
def create_event(
    event: EventCreate, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)
):
    """Create a new event."""
    repo = SQLEventRepository(session)
    return repo.create_event(event)


@router.get(
    "/search/",
    response_model=List[Event],
    description="Search events by name",
    status_code=status.HTTP_200_OK,
)
def search_events(name: str, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """Search events by name."""
    repo = SQLEventRepository(session)
    return repo.search_events(name)


@router.get(
    "/",
    response_model=list[Event],
    description="Get all events",
    status_code=status.HTTP_200_OK,
)
def get_events(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """Get all events."""
    repo = SQLEventRepository(session)
    return repo.get_events()


@router.get(
    "/{event_id}",
    response_model=Event,
    description="Get an event",
    status_code=status.HTTP_200_OK,
)
def get_event(event_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """Get an event by ID."""
    repo = SQLEventRepository(session)
    event = repo.get_event_by_id(event_id)
    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return event


@router.patch(
    "/{event_id}",
    response_model=Event,
    description="Update an event",
    status_code=status.HTTP_200_OK,
)
def update_event(
    event_id: int,
    event: EventUpdate,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    """Update an event by ID."""
    repo = SQLEventRepository(session)
    updated_event = repo.update_event(event_id, event)
    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return updated_event


@router.delete(
    "/{event_id}",
    response_model=Event,
    description="Inactivate an event",
    status_code=status.HTTP_200_OK,
)
def inactivate_event(
    event_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)
):
    """Inactivate an event by ID."""
    repo = SQLEventRepository(session)
    updated_event = repo.inactivate_event(event_id)
    if not updated_event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")
    return updated_event


@router.post("/{event_id}/register", status_code=status.HTTP_201_CREATED, description="Register an event")
def register_user_to_event(
    event_id: int, session: Session = Depends(get_session), current_user: User = Depends(get_current_user)
):
    """Register the current user to an event."""
    event_repo = SQLEventRepository(session)
    reg_repo = SQLRegistrationRepository(session)

    event = event_repo.get_event_by_id(event_id)

    if not event:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Event not found")

    if not event.state:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event is inactive")

    if reg_repo.is_user_registered(current_user.id, event.id):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User already registered for this event")

    current_count = reg_repo.count_registrations(event.id)

    if current_count >= event.capacity:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Event is at full capacity")

    return reg_repo.register_user(current_user.id, event.id)


@router.get(
    "/me/events",
    response_model=List[Event],
    description="Get events the current user is registered for",
    status_code=status.HTTP_200_OK,
)
def get_my_events(session: Session = Depends(get_session), current_user: User = Depends(get_current_user)):
    """Get events the current user is registered for."""
    reg_repo = SQLRegistrationRepository(session)
    return reg_repo.get_user_events(current_user.id)
