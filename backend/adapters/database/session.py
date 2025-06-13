"""Module for managing database sessions using SQLModel."""

from sqlmodel import Session, create_engine

from config import settings

engine = create_engine(settings.DATABASE_URL, echo=True)


def get_session():
    """Initialize the session."""
    with Session(engine) as session:
        yield session
