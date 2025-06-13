"""Database session management for SQLModel."""

from typing import Optional

from sqlmodel import Field, SQLModel


class EventRegistration(SQLModel, table=True):
    """Model representing an event registration."""

    id: Optional[int] = Field(None, primary_key=True)
    event_id: int = Field(foreign_key="event.id")
    user_id: int = Field(foreign_key="user.id")
