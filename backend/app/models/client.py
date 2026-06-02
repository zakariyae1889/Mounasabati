from sqlalchemy import Column,Integer,String,ForeignKey,Text,DateTime
from sqlalchemy.orm import relationship
from app.core.database import Base

import datetime



class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    
    phone = Column(String, index=True,nullable=True)
    city = Column(String, index=True,nullable=True)
    address = Column(String, index=True,nullable=True)

    user = relationship("User", back_populates="client_profile")

    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
