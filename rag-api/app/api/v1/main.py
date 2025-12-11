from fastapi import FastAPI

from app.api.v1.endpoints import document, user, chat

app = FastAPI()

app.include_router(document.router, prefix="/api/v1/docs", tags=["docs"])
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(chat.router, prefix="/api/v1/chats", tags=["chats"])
