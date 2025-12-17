from typing import Optional

from sqlalchemy.orm import Session

from app.models.document import Document
from app.schemas.document import *


def create_document(
    request: DocRegRequest, db: Session, user_id: int, url: str
) -> Document:
    doc = Document(
        user_id=user_id,
        title=request.title,
        url=url,
        size=len(request.file),
    )
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


def get_documents(
        db: Session, user_id: int
) -> list[Document]:
    return db.query(Document).filter(Document.user_id == user_id).all()


def get_document_by_id(
        db: Session, user_id: int, document_id: int
) -> Optional[Document]:
    return db.query(Document).filter(Document.user_id == user_id).filter(Document.id == document_id).first()
