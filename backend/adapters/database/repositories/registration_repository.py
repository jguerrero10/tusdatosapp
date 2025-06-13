"""Database session management for SQLModel."""

from typing import List

from sqlmodel import Session, select

from core.entities.event import Event
from core.entities.registration import EventRegistration


class SQLRegistrationRepository:
    """Repository for managing event registrations in the database."""

    def __init__(self, session: Session):
        """Initialize the SQLRegistrationRepository with a database session."""
        self.session = session

    def is_user_registered(self, user_id: int, event_id: int) -> bool:
        """Check if a user is registered for a specific event."""
        stmt = select(EventRegistration).where(
            EventRegistration.user_id == user_id, EventRegistration.event_id == event_id
        )
        return self.session.exec(stmt).first() is not None

    def count_registrations(self, event_id: int) -> int:
        """Count the number of registrations for a specific event."""
        stmt = select(EventRegistration).where(EventRegistration.event_id == event_id)
        return len(self.session.exec(stmt).all())

    def get_user_events(self, user_id: int) -> List[Event]:
        """Get all events a user is registered for."""
        stmt = select(Event).join(EventRegistration).where(EventRegistration.user_id == user_id)
        return self.session.exec(stmt).all()

    def register_user(self, user_id: int, event_id: int) -> EventRegistration:
        """Register a user for an event."""
        registration = EventRegistration(user_id=user_id, event_id=event_id)
        self.session.add(registration)
        self.session.commit()
        self.session.refresh(registration)
        return registration
