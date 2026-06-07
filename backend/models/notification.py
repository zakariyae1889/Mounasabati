from __future__ import annotations
import uuid
from uuid import UUID
from datetime import datetime,timezone
from typing import Optional,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship,Column,ForeignKey

if TYPE_CHECKING:
    from .user import User


class Notification(SQLModel, table=True):
    __tablename__ = "notifications"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    user_id: UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False))
    
    title: str = Field(nullable=False)
    body: str = Field(nullable=False)
    is_read: bool = Field(default=False, nullable=False)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc)) # تم تصحيح الكلمة الإملائية updateed_at

    user: "User" = Relationship(back_populates="notifications")