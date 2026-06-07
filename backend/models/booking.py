from __future__ import annotations
from typing import Optional,List,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship,Column,ForeignKey

import datetime
from datetime import datetime, date, time,timezone
import uuid
from uuid import UUID
import enum

if TYPE_CHECKING:
    from .user import User
    from .service import Service
    from .payment import Payment

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
    service_id: UUID = Field(sa_column=Column(ForeignKey("services.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False))
    user_id: UUID = Field(sa_column=Column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"), nullable=False))
    
    event_date: date = Field(nullable=False)
    event_time: time = Field(nullable=False)
    total_price: float = Field(default=0.00)
    status: BookingStatus = Field(default=BookingStatus.pending)
    
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    user: "User" = Relationship(back_populates="bookings")
    service: "Service" = Relationship(back_populates="bookings")
    payments: List["Payment"] = Relationship(back_populates="booking")






