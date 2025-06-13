"""SQL repository for the Event entity."""

from typing import List

from sqlmodel import Session, select

from core.entities.event import Event, EventCreate, EventUpdate
from core.ports.repositories.event_repository import EventRepository


class SQLEventRepository(EventRepository):
    """SQL repository for the Event entity."""

    def __init__(self, session: Session):
        """Initialize the SQL event repository."""
        self.session = session

    def get_events(self) -> List[Event]:
        """Retrieve all events from the database."""
        stmt = select(Event)
        return self.session.exec(stmt).all()

    def get_event_by_id(self, event_id: int) -> type[Event] | None:
        """Retrieve an event by its ID."""
        stmt = select(Event).where(Event.id == event_id)
        return self.session.exec(stmt).first()

    def create_event(self, event: EventCreate) -> Event:
        """Create a new event in the database."""
        db_event = Event(**dict(event))
        self.session.add(db_event)
        self.session.commit()
        self.session.refresh(db_event)
        return db_event

    def search_events(self, name: str) -> List[Event]:
        """Search for events by name."""
        stmt = select(Event).where(Event.name.contains(name))
        return self.session.exec(stmt).all()

    def update_event(self, event_id: int, event: EventUpdate) -> type[Event] | None:
        """Update an existing event in the database."""
        existing_event = self.get_event_by_id(event_id)
        if not existing_event:
            return None

        event_update = {key: value for key, value in dict(event).items() if value is not None}

        for attr, value in event_update.items():
            setattr(existing_event, attr, value)

        self.session.add(existing_event)
        self.session.commit()
        self.session.refresh(existing_event)
        return existing_event

    def inactivate_event(self, event_id: int) -> type[Event] | None:
        """Inactivate an event by setting its state to False."""
        event_state = EventUpdate(state=False)
        return self.update_event(event_id, event_state)
