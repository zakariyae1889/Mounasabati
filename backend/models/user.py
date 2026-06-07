from __future__ import annotations
import enum
from datetime import datetime,timezone
from typing import Optional, List,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship
import uuid
from uuid import UUID

if TYPE_CHECKING:
    from .client import Client
    from .vendor import Vendor
    from .reviews import Review
    from .booking import Booking
    from .notification import Notification
    from .payment import Payment


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
   
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

   
    client_profile: Optional["Client"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    vendor_profile: Optional["Vendor"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    
   
   
    reviews: List["Review"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    bookings: List["Booking"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"}) 
    notifications: List["Notification"] = Relationship(back_populates="user", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    payments: List["Payment"] = Relationship(back_populates="user")