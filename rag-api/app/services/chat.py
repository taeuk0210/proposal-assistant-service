from sqlalchemy.orm import Session

from app.schemas.chats import *
from app.clients.openai import gpt2


def send_message(request: ChatRequest, db: Session) -> ChatResponse:
    response = gpt2.send_message(request.content)
    return ChatResponse(content=response)
