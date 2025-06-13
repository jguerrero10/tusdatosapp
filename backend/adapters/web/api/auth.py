"""Database session management for SQLModel."""

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlmodel import Session

from adapters.database.repositories.user_repository import SQLUserRepository
from adapters.database.session import get_session
from core.entities.user import UserCreate, UserRead, User
from core.security.auth import create_access_token, verify_password
from core.security.dependencies import get_current_user

router = APIRouter()


@router.post("/register", response_model=UserRead)
def register(user: UserCreate, session: Session = Depends(get_session)):
    """Register a new user."""
    repo = SQLUserRepository(session)
    existing_user = repo.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return repo.create_user(user)

@router.post("/register-speaker")
def register_speaker(current_user: User = Depends(get_current_user), session: Session = Depends(get_session)):
    repo = SQLUserRepository(session)
    repo.register_user_like_speaker(current_user)
    return {"message": "User registered as speaker"}

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(get_session)):
    """Login a user and return an access token."""
    repo = SQLUserRepository(session)
    user = repo.get_user_by_email(form_data.username)
    if not user or not verify_password(form_data.password, user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    token = create_access_token(data={"sub": str(user.email)})
    return {"access_token": token, "token_type": "bearer"}
