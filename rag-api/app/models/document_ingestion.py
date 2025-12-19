from datetime import datetime

from sqlalchemy import text, String, DateTime, func, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class DocumentIngestion(Base):
    __tablename__ = "document_ingestions"

    id: Mapped[int] = mapped_column(
        Integer(),
        primary_key=True,
    )

    user_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    document_id: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    embedding_model: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    embedding_dim: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
    )

    state: Mapped[str] = mapped_column(
        String(20),
        default="PENDING",
        server_default=text("'PENDING'"),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )
