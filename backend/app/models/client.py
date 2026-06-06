from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
import uuid
from uuid import UUID
from app.models import User



class Client(SQLModel, table=True):
    __tablename__ = "clients"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)
    
    phone: Optional[str] = Field(default=None, index=True)
    city: Optional[str] = Field(default=None, index=True)
    address: Optional[str] = Field(default=None, index=True)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # تم التصحيح: back_populates يشير إلى الحقل المتواجد في User
    user: Optional["User"] = Relationship(back_populates="client_profile")