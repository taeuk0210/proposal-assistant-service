from typing import Optional

from sqlalchemy.orm import Session

from app.models.document_info import DocumentInfo
from app.schemas.document import *


def create_document(
    request: DocRegRequest, db: Session, user_id: int, url: str
) -> DocumentInfo:
    doc = DocumentInfo(
        user_id=user_id,
        title=request.title,
        url=url,
        size=len(request.file),
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


def get_documents(db: Session, user_id: int) -> list[DocumentInfo]:
    return db.query(DocumentInfo).filter(DocumentInfo.user_id == user_id).all()


def get_document_by_id(
    db: Session, user_id: int, document_id: int
) -> Optional[DocumentInfo]:
    return (
        db.query(DocumentInfo)
        .filter(DocumentInfo.user_id == user_id)
        .filter(DocumentInfo.id == document_id)
        .first()
    )
