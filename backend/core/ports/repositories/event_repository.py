"""Interface for event repository."""

from abc import ABC, abstractmethod
from typing import List

from core.entities.event import Event, EventCreate, EventUpdate


class EventRepository(ABC):
    """Abstract base class for event repository."""

    @abstractmethod  # pragma: no cover
    def get_event_by_id(self, event_id: int) -> Event:
        """Retrieve an event by its ID."""
        pass

    @abstractmethod  # pragma: no cover
    def get_events(self) -> List[Event]:
        """Retrieve all events."""
        pass

    @abstractmethod  # pragma: no cover
    def create_event(self, event: EventCreate) -> Event:
        """Create a new event."""
        pass

    @abstractmethod  # pragma: no cover
    def update_event(self, event_id: int, event: EventUpdate) -> Event:
        """Update an existing event."""
        pass

    @abstractmethod  # pragma: no cover
    def search_events(self, nombre: str) -> List[Event]:
        """Search for events by name."""
        pass
