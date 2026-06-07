
from __future__ import annotations
from typing import Optional,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship,Column,ForeignKey,CheckConstraint

from datetime import datetime, timezone
import uuid
from uuid import UUID

if TYPE_CHECKING:
    from .user import User
    from .service import Service




class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    service_id: UUID = Field(sa_column=Column(ForeignKey("services.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False))
    user_id: UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False))

    rating: int = Field(nullable=False)

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user: "User" = Relationship(back_populates="reviews")
    service: "Service" = Relationship(back_populates="reviews")

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

