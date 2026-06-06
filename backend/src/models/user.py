import enum
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

import uuid
from uuid import UUID
from src.models.client import Client
from src.models.vendor import Vendor
from src.models.reviews import Review
from src.models.booking import Booking
from src.models.payment import Payment
from src.models.notification import Notification
class UserRole(str, enum.Enum):
    client = "client"
    vendor = "vendor"






class UserRole(str, enum.Enum):
    client = "client"
    vendor = "vendor"

class User(SQLModel, table=True):
    __tablename__ = "users"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False, unique=True)
    username: str = Field(unique=True, index=True, nullable=False)
    email: str = Field(unique=True, index=True, nullable=False)
    password: str = Field(nullable=False)
    CIN: str = Field(unique=True, index=True, nullable=False)
    
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    role: UserRole = Field(default=UserRole.client)
    image: str = Field(default="default_service.png")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    # تم تصحيح back_populates ليرتبط بـ اسم الحقل الفعلي في الجداول الأخرى
    client_profile: Optional["Client"] = Relationship(back_populates="user")
    vendor_profile: Optional["Vendor"] = Relationship(back_populates="user")
    reviews: List["Review"] = Relationship(back_populates="user")
    bookings: List["Booking"] = Relationship(back_populates="user") 
    notifications: List["Notification"] = Relationship(back_populates="user")
    payment: List["Payment"] = Relationship(back_populates="user")