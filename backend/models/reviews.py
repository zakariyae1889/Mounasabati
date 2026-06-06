
from __future__ import annotations
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship,CheckConstraint

from datetime import datetime, timezone
import uuid
from uuid import UUID




class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    service_id: UUID = Field(foreign_key="services.id", nullable=False)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)

    rating: int = Field(nullable=False) # التقييم إجباري من 1 لـ 5

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user: Optional["User"] = Relationship(back_populates="reviews")
    service: Optional["Service"] = Relationship(back_populates="reviews")

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )


    

