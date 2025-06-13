"""Database session management for SQLModel."""

from typing import Optional

from sqlmodel import Field, SQLModel


class UserBase(SQLModel):
    """Base model for user entities."""

    email: str = Field(..., index=True, unique=True)
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """Model for creating a new user."""

    password: str


class UserLogin(SQLModel):
    """Model for user login."""

    email: str
    password: str


class User(UserBase, table=True):
    """Model representing a user in the database."""

    id: Optional[int] = Field(default=None, primary_key=True)
    hashed_password: str
    is_speaker: bool = Field(default=False, description="Indicates if the user is a speaker.")

class UserRead(UserBase):
    """Model for reading user data."""

    id: int
