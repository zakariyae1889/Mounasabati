from sqlalchemy import Column,Integer,String,Enum,DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum

import datetime


class UserRole(enum.Enum):
    client="client"
    vendor="vendor"


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name = Column(String, index=True, nullable=True)
    last_name = Column(String, index=True, nullable=True)
    email = Column(String, unique=True, index=True)
    CIN = Column(String, unique=True, index=True)
    role = Column(Enum(UserRole), default=UserRole.client) 
    password = Column(String)
    image = Column(String, nullable=True, default="default_service.png")
    client_profile = relationship("Client", back_populates="user")
    bookings = relationship("Booking", back_populates="user")

    created_at = Column(DateTime,default=datetime.datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.datetime.utcnow)



