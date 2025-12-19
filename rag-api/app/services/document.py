from fastapi.responses import FileResponse

from sqlalchemy.orm import Session

from app.schemas.document import *
from app.exceptions.document import *
from app.indices import qdrant
from app.clients.embed import client
from app.stores import file_storage
from app.services import chunk as chunk_service
from app.repositories import document_info as docs_repository
from app.repositories import document_ingestion as ings_repository
from app.repositories import chunk_info as chunk_repository


async def register_document(
    request: DocRegRequest,
    db: Session,
    user_id: int,
) -> DocRegResponse:

    # save file
    url = file_storage.save(request.title, request.file)

    # save meta
    doc = docs_repository.create_document(request, db, user_id, url)
    doc = DocResponse.model_validate(doc)
    ing = ings_repository.create_ingestion(
        IngRegRequest(
            document_id=doc.id,
            embedding_dim=1024,
            embedding_model="dragonkue/bge-m3-ko",
        ),
        db,
        user_id,
    )
    ing = IngResponse.model_validate(ing)

    # chunking
    chunks = chunk_service.chunking(doc, ing)

    # embedding
    for chunk in chunks:
        chunk.point.embedding = await client.get_embedding(chunk.point.content)

    # save chunk
    for chunk in chunks:
        chunk_meta = chunk_repository.create_chunk(chunk.meta, db, user_id)
        qdrant.upsert_documents(chunk_meta.id, chunk)

    return DocRegResponse()


def get_documents(db: Session, user_id: int) -> DocListResponse:
    docs = docs_repository.get_documents(db, user_id)
    items = [DocResponse.model_validate(d) for d in docs]
    return DocListResponse(items=items, total=len(items))


def get_document_file(document_id: int, db: Session, user_id: int) -> bytes:
    doc = docs_repository.get_document_by_id(db, user_id, document_id)
    return FileResponse(path=doc.url, media_type="application/pdf")
