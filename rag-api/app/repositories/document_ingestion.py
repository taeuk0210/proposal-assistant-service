from typing import Optional

from sqlalchemy.orm import Session

from app.models.document_ingestion import DocumentIngestion
from app.schemas.document import *


def create_ingestion(request: IngRegRequest, db: Session, user_id: int):
    ingestion = DocumentIngestion(
        user_id=user_id,
        document_id=request.document_id,
        embedding_model=request.embedding_model,
        embedding_dim=request.embedding_dim,
    )
    db.add(ingestion)
    db.commit()
    db.refresh(ingestion)
    return ingestion
