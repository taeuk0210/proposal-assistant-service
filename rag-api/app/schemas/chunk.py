from pydantic import BaseModel


class MetaRegRequest(BaseModel):
    document_id: int
    ingestion_id: int
    chunk_index: int
    page_start: int
    page_end: int


class PointRegRequest(BaseModel):
    content: str
    embedding: list[float]


class ChunkRegRequest(BaseModel):
    meta: MetaRegRequest
    point: PointRegRequest
