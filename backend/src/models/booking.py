
from typing import Optional,List
from sqlmodel import SQLModel, Field, Relationship

import datetime
from datetime import datetime, date, time
import uuid
from uuid import UUID
import enum

from src.models.user import User
from src.models.service import Service
from src.models.payment import Payment
class BookingStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    paid = "paid"
    cancelled = "cancelled"




class BookingStatus(str, enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    cancelled = "cancelled"

class Booking(SQLModel, table=True):
    __tablename__ = "bookings"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False, unique=True)
    service_id: UUID = Field(foreign_key="services.id", nullable=False)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)
    
    event_date: date = Field(nullable=False)
    event_time: time = Field(nullable=False)
    total_price: float = Field(default=0.00)
    status: BookingStatus = Field(default=BookingStatus.pending)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    user: Optional["User"] = Relationship(back_populates="bookings")
    service: Optional["Service"] = Relationship(back_populates="bookings")


    payment: List["Payment"] = Relationship(back_populates="bookings")






