from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from app.schemas.document import *
from app.exceptions.document import *
from app.repositories import document as docs_repository
from app.stores import file_storage


def register_document(
    request: DocRegRequest,
    db: Session,
    user_id: int,
) -> DocRegResponse:
    url = file_storage.save(request.title, request.file)
    docs_repository.create_document(request, db, user_id, url)
    return DocRegResponse()


def get_documents(
    db: Session, user_id: int
) -> DocListResponse:
    docs = docs_repository.get_documents(db, user_id)
    items = [DocResponse.model_validate(d) for d in docs]
    return DocListResponse(items=items, total=len(items))

def get_document_file(
    document_id: int, db: Session, user_id: int
) -> bytes:
    doc = docs_repository.get_document_by_id(db, user_id, document_id)
    return FileResponse(path=doc.url, media_type="application/pdf")
