from sqlalchemy import Column,Integer,ForeignKey,Date,Time,DECIMAL,Enum,DateTime

from sqlalchemy.orm import relationship
from app.core.database import Base

import enum

import datetime


class BookingStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    paid = "paid"
    cancelled = "cancelled"



class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey("services.id")) 
    user_id = Column(Integer, ForeignKey("users.id"))

    event_date = Column(Date, index=True, nullable=False) 
    event_time = Column(Time, index=True, nullable=False)
    total_price = Column(DECIMAL(10, 2), default=0.00)
    status = Column(Enum(BookingStatus), default=BookingStatus.pending)

    user = relationship("User", back_populates="bookings")
    service = relationship("Service", back_populates="bookings")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.datetime.utcnow)


