from sqlalchemy import Column,Integer,String,ForeignKey,Enum,DECIMAL,Text,DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
import datetime

import enum

class ServiceStatus(enum.Enum): # غيرت الاسم لتجنب التكرار مع Status الحجز
    active = "active"
    inactive = "inactive"

class Service(Base):
    __tablename__ = "services"
    id = Column(Integer, primary_key=True, index=True)
    vendor_id = Column(Integer, ForeignKey("vendors.id"))

    ServiceName = Column(String, index=True)
    price_base = Column(DECIMAL(10, 2), default=0.00) # إضافة أرقام عشرية
    status = Column(Enum(ServiceStatus), default=ServiceStatus.active)
    description = Column(Text, nullable=True)
    image = Column(String, nullable=True, default="default_service.png")
    slug = Column(String, unique=True, index=True)
    vendor = relationship("Vendor", back_populates="services")
    bookings = relationship("Booking", back_populates="service")


    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.datetime.utcnow)