import PyPDF2

from app.schemas.chunk import *
from app.schemas.document import *


def chunking(doc: DocResponse, ing: IngResponse) -> list[ChunkRegRequest]:
    # Todo: text 추출 및 청킹 전략 고도화

    reader = PyPDF2.PdfReader(doc.url)

    return [
        ChunkRegRequest(
            meta=MetaRegRequest(
                document_id=doc.id,
                ingestion_id=ing.id,
                chunk_index=chunk_index,
                page_start=chunk_index + 1,
                page_end=chunk_index + 1,
            ),
            point=PointRegRequest(content=page.extract_text(), embedding=[]),
        )
        for chunk_index, page in enumerate(reader.pages)
    ]
