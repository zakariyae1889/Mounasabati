from __future__ import annotations
from datetime import datetime,timezone
from typing import Optional, List,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
import uuid
from uuid import UUID

if TYPE_CHECKING:
    from .user import User
    from .service import Service




class Vendor(SQLModel, table=True):
    __tablename__ = "vendors"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)

    phone: Optional[str] = Field(index=True)
    city: Optional[str] = Field(index=True)
    address: Optional[str] = Field(index=True)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user: Optional["User"] = Relationship(back_populates="vendor_profile")
    services: List["Service"] = Relationship(back_populates="vendor")



