from __future__ import annotations
from datetime import datetime,timezone
from typing import Optional,TYPE_CHECKING
from sqlmodel import SQLModel, Field, Relationship,Column,ForeignKey

import enum
import uuid
from uuid import UUID

if TYPE_CHECKING:
    from .user import User
    from .booking import Booking


class PaymentStatus(str,enum.Enum):
    Pending="pending"
    Success="success"
    Failed="failed"



class Payment(SQLModel, table=True):
    __tablename__ = "payments"
    
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False, unique=True)
    
   
    booking_id: Optional[UUID] = Field(sa_column=Column(ForeignKey("bookings.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True))
    user_id: Optional[UUID] = Field(sa_column=Column(ForeignKey("users.id", ondelete="SET NULL", onupdate="CASCADE"), nullable=True))
    
    amount: float = Field(default=0.00)
    currency: str = Field(default="MAD")
    paymentStatus: PaymentStatus = Field(default=PaymentStatus.Pending)
    TransactionID: Optional[str] = Field(default=None, index=True)

    user: Optional["User"] = Relationship(back_populates="payments")
    booking: Optional["Booking"] = Relationship(back_populates="payments")

    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
