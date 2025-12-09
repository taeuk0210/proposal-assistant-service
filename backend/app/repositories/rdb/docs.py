from typing import Optional, List

from sqlalchemy.orm import Session

from app.models.docs import Document
from app.schemas.docs import *


def get_document_by_id(db: Session, document_id: int) -> Optional[Document]:
    doc = db.query(Document).filter(Document.document_id == document_id).first()
    return DocumentInfo.model_validate(doc)


def create_document(db: Session, data: DocumentCreate) -> Document:
    doc = Document(title=data.title, file_path=data.file_path, user_id=data.user_id)
    db.add(doc)
    db.commit()
    db.refresh(doc)
    return doc


def get_documents_by_title(
    db: Session, query: str, page: int, num_items: int
) -> List[Document]:

    return (
        db.query(Document)
        .filter(Document.title.like(f"%{query}%"))
        .offset((page - 1) * num_items)
        .limit(num_items)
        .all()
    )
