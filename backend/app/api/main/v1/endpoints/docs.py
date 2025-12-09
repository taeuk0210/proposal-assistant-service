from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.core.security import get_current_user_id
from app.schemas.docs import *
from app.services import docs as docs_service

router = APIRouter()


@router.post(
    "/",
    response_model=DocumentInfo,
    status_code=status.HTTP_201_CREATED,
)
def register_document(
    data: DocumentBase,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
) -> DocumentInfo:
    return docs_service.register_document(db, data, user_id)


@router.get("/", response_model=List[DocumentInfo], status_code=status.HTTP_200_OK)
def get_documents(
    query: str = "", page: int = 1, num_items: int = 20, db: Session = Depends(get_db)
) -> List[DocumentInfo]:
    return docs_service.get_documents_by_title(db, query, page, num_items)
