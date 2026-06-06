
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship,CheckConstraint

import datetime
import uuid
from uuid import UUID

from src.models.user import User
from src.models.service import Service

import uuid
from uuid import UUID
from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel, Field, Relationship, CheckConstraint

class Review(SQLModel, table=True):
    __tablename__ = "reviews"

    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False)
    service_id: UUID = Field(foreign_key="services.id", nullable=False)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)

    rating: int = Field(nullable=False) # التقييم إجباري من 1 لـ 5

    created_at: datetime = Field(default_factory=datetime.utcnow)  
    updated_at: datetime = Field(default_factory=datetime.utcnow)  

    user: Optional["User"] = Relationship(back_populates="reviews")
    service: Optional["Service"] = Relationship(back_populates="reviews")

    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )


    

