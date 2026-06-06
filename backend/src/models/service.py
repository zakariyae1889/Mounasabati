import enum
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship

import datetime
import uuid
from uuid import UUID
import enum


from src.models.vendor import Vendor
from src.models.reviews import Review
from src.models.booking import Booking
from src.models.client import Client



class ServiceStatus(enum.Enum): # غيرت الاسم لتجنب التكرار مع Status الحجز
    active = "active"
    inactive = "inactive"

import uuid
from uuid import UUID
from datetime import datetime
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
import enum

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
    
    created_at: datetime = Field(default_factory=datetime.utcnow)  
    updated_at: datetime = Field(default_factory=datetime.utcnow)   

    # العلاقات العكسية الصحيحة
    vendor: Optional["Vendor"] = Relationship(back_populates="services")
    bookings: List["Booking"] = Relationship(back_populates="service")
    reviews: List["Review"] = Relationship(back_populates="service")