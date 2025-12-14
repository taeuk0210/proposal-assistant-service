from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.cores.database import get_db
from app.cores.security import get_current_user_id
from app.schemas.chat import *
from app.services import chat as chat_service

router = APIRouter()


@router.post(
    "/",
    response_model=ChatResponse,
    status_code=status.HTTP_201_CREATED,
)
def chat(
    request: ChatRequest,
    db: Session = Depends(get_db),
    user_id: str = Depends(get_current_user_id),
) -> ChatResponse:
    return chat_service.send_message(request, db)
