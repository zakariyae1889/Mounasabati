from __future__ import annotations
import enum
from datetime import datetime,timezone
from typing import Optional, List,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship,Column,ForeignKey


import uuid
from uuid import UUID
import enum


if TYPE_CHECKING:
    from .vendor import Vendor
    from .booking import Booking
    from .reviews import Review




class ServiceStatus(enum.Enum): # غيرت الاسم لتجنب التكرار مع Status الحجز
    active = "active"
    inactive = "inactive"



class ServiceStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"

class Service(SQLModel, table=True):
    __tablename__ = "services"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False, unique=True)
   
    vendor_id: UUID = Field(sa_column=Column(ForeignKey("vendors.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False))
    
    name: str = Field(index=True)
    description: Optional[str] = Field(default=None)
    price: float = Field(default=0.0)
    image: str = Field(default="default_service.png")
    status: ServiceStatus = Field(default=ServiceStatus.active, nullable=False)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))   

    vendor: "Vendor" = Relationship(back_populates="services")
    bookings: List["Booking"] = Relationship(back_populates="service", sa_relationship_kwargs={"cascade": "all, delete-orphan"})
    reviews: List["Review"] = Relationship(back_populates="service", sa_relationship_kwargs={"cascade": "all, delete-orphan"})