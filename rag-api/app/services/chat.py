from sqlalchemy.orm import Session

from app.schemas.chat import *
from app.clients.qwen import qwen


def send_message(request: ChatRequest, db: Session) -> ChatResponse:
    reply = qwen.send_message(request.message)
    return ChatResponse(reply=reply)
