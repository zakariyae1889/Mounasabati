from __future__ import annotations

from datetime import datetime,timezone
from typing import Optional,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship,Column,ForeignKey

import uuid
from uuid import UUID


if TYPE_CHECKING:
    from .user import User



class Client(SQLModel, table=True):
    __tablename__ = "clients"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    user_id: UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False))
    
    phone: Optional[str] = Field(default=None, index=True)
    city: Optional[str] = Field(default=None, index=True)
    address: Optional[str] = Field(default=None, index=True)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    image: Optional[str] = Field(default="default_service.png")

    user: "User" = Relationship(back_populates="client_profile")