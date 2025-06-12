"""Database session management for SQLModel."""

from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class EventBase(SQLModel):
    """Base model for the Event entity."""

    name: str = Field(..., title="Name", description="The name of the event.")
    description: str = Field(..., title="Description", description="A brief description of the event.")
    capacity: int = Field(
        ...,
        title="Capacity",
        description="The maximum number of participants allowed in the event.",
    )
    start_date: datetime = Field(..., title="Start Date", description="The date and time when the event starts.")
    end_date: datetime = Field(..., title="End Date", description="The date and time when the event ends.")
    state: Optional[bool] = Field(True, title="State", description="The current state of the event.")


class EventUpdate(EventBase):
    """Model for updating an existing event."""

    name: Optional[str] = Field(None, title="Name", description="The name of the event.")
    description: Optional[str] = Field(None, title="Description", description="A brief description of the event.")
    capacity: Optional[int] = Field(
        None,
        title="Capacity",
        description="The maximum number of participants allowed in the event.",
    )
    start_date: Optional[datetime] = Field(
        None, title="Start Date", description="The date and time when the event starts."
    )
    end_date: Optional[datetime] = Field(None, title="End Date", description="The date and time when the event ends.")
    state: Optional[bool] = Field(None, title="State", description="The current state of the event.")


class Event(EventBase, table=True):
    """Model representing an event in the database."""

    id: Optional[int] = Field(default=None, primary_key=True)


class EventCreate(EventBase):
    """Model for creating a new event."""

    pass
