from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from adapters.database.session import get_session
from core.entities.user import User

router = APIRouter()

@router.get("/speakers", response_model=List[User])
def get_speakers(session: Session = Depends(get_session)):
    stmt = select(User).where(User.is_speaker == True)
    return session.exec(stmt).all()