from __future__ import annotations
import enum
from datetime import datetime,timezone
from typing import Optional, List,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship


import uuid
from uuid import UUID
import enum


if TYPE_CHECKING:
    from .vendor import Vendor
    from .booking import Booking




class ServiceStatus(enum.Enum): # غيرت الاسم لتجنب التكرار مع Status الحجز
    active = "active"
    inactive = "inactive"



class ServiceStatus(str, enum.Enum):
    active = "active"
    inactive = "inactive"

class Service(SQLModel, table=True):
    __tablename__ = "services"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False, unique=True)
    vendor_id: UUID = Field(foreign_key="vendors.id", nullable=False)
    
    name: str = Field(index=True)
    description: Optional[str] = Field(default=None)
    price: float = Field(default=0.0)
    image: str = Field(default="default_service.png")
    status: ServiceStatus = Field(default=ServiceStatus.active, nullable=False)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))  
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))   

    # العلاقات العكسية الصحيحة
    vendor: Optional["Vendor"] = Relationship(back_populates="services")
    bookings: List["Booking"] = Relationship(back_populates="service")
    reviews: List["Review"] = Relationship(back_populates="service")