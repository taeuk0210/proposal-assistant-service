from datetime import datetime
from pydantic import BaseModel


class DocRegRequest(BaseModel):
    title: str
    file: bytes


class DocRegResponse(BaseModel):
    ok: bool = True


class DocResponse(BaseModel):
    id: int
    user_id: int
    title: str
    url: str
    size: int
    created_at: datetime

    model_config = {
        "from_attributes": True
    }


class DocListResponse(BaseModel):
    items: list[DocResponse]
    total: int