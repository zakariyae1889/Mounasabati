from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel,Field,Relationship

import enum
import uuid
from uuid import UUID
from src.models.user import User
from src.models.booking import Booking
class PaymentStatus(str,enum.Enum):
    Pending="pending"
    Success="success"
    Failed="failed"



class Payment(SQLModel,table=True):
    __tablename__="payments"
    id: UUID = Field(default_factory=uuid.uuid4, primary_key=True, index=True, nullable=False, unique=True)
    booking_id:UUID=Field(foreign_key="bookings.id",nullable=False)
    user_id: UUID = Field(foreign_key="users.id", nullable=False)
    amount:float=Field(default=0.00)
    currency:str=Field(default="MAD")
    paymentStatus:PaymentStatus=Field(default=PaymentStatus.Pending)
    TransactionID: Optional[str] = Field(default=None, index=True)

    user: Optional["User"] = Relationship(back_populates="user")
    booking: Optional["Booking"] = Relationship(back_populates="bookings")

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
