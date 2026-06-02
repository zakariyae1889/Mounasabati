from sqlalchemy import Column,Integer,ForeignKey,String,DECIMAL,Enum
from sqlalchemy.orm import relationship
from app.core.database import Base

import enum

class BookingStatus(enum.Enum):
    pending = "pending"
    confirmed = "confirmed"
    paid = "paid"
    cancelled = "cancelled"



class Booking(Base):
    __tablename__ = "bookings"
    id = Column(Integer, primary_key=True, index=True)
    service_id = Column(Integer, ForeignKey("services.id")) # تصحيح كلمة services
    user_id = Column(Integer, ForeignKey("users.id"))

    event_date = Column(String, index=True) 
    event_time =Column(String,index=True)
    total_price = Column(DECIMAL(10, 2), default=0.00)
    status = Column(Enum(BookingStatus), default=BookingStatus.pending)

    user = relationship("User", back_populates="bookings")
    service = relationship("Service", back_populates="bookings")

