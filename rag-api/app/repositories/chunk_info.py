from typing import Optional

from sqlalchemy.orm import Session

from app.models.chunk_info import ChunkInfo
from app.schemas.chunk import *


def create_chunk(request: MetaRegRequest, db: Session, user_id: int):
    chunk = ChunkInfo(
        user_id=user_id,
        document_id=request.document_id,
        ingestion_id=request.ingestion_id,
        chunk_index=request.chunk_index,
        page_start=request.page_start,
        page_end=request.page_end,
    )
    db.add(chunk)
    db.commit()
    db.refresh(chunk)
    return chunk
