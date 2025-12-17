from io import BytesIO

from fastapi import APIRouter, Depends, status, UploadFile, Form, File
from fastapi.responses import FileResponse
from sqlalchemy.orm import Session

from app.cores.database import get_db
from app.cores.security import get_current_user_id
from app.schemas.document import *
from app.services import document as docs_service

router = APIRouter()


@router.post(
    "/",
    response_model=DocRegResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register_document(
    title: str = Form(...),
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
) -> DocRegResponse:
    request = DocRegRequest(title=title, file=await file.read())
    return docs_service.register_document(request, db, user_id)


@router.get(
    "/",
    response_model=DocListResponse,
    status_code=status.HTTP_200_OK,
)
def get_documents(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
) -> DocRegResponse:    
    return docs_service.get_documents(db, user_id)


@router.get(
    "/{document_id}",
    # response_model=FileResponse,
    status_code=status.HTTP_200_OK,
)
def get_documents(
    document_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id),
) -> FileResponse:    
    return docs_service.get_document_file(document_id, db, user_id)