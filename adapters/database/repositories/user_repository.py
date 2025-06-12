"""Database session management for SQLModel."""

from sqlmodel import Session, select

from core.entities.user import User, UserCreate
from core.security.auth import hash_password


class SQLUserRepository:
    """Repository for managing users in the database."""

    def __init__(self, session: Session):
        """Initialize the SQLUserRepository with a database session."""
        self.session = session

    def create_user(self, user_create: UserCreate) -> User:
        """Create a new user in the database."""
        user = User(
            email=user_create.email,
            full_name=user_create.full_name,
            hashed_password=hash_password(user_create.password),
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_email(self, email: str) -> User | None:
        """Retrieve a user by their email address."""
        statement = select(User).where(User.email == email)
        return self.session.exec(statement).first()
