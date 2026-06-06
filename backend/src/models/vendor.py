from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
import uuid
from uuid import UUID
from src.models.user import User
from src.models.service import Service


import uuid
from uuid import UUID
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

class Vendor(SQLModel, table=True):
    __tablename__ = "vendors"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)

    phone: Optional[str] = Field(index=True)
    city: Optional[str] = Field(index=True)
    address: Optional[str] = Field(index=True)
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional["User"] = Relationship(back_populates="vendor_profile")
    services: List["Service"] = Relationship(back_populates="vendor")



