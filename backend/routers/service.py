from sqlalchemy import Column,Integer,String,ForeignKey,Text,Enum,DECIMAL
from sqlalchemy.orm import relationship
from app.core.database import Base

import enum

class Status(enum.Enum):
    active="active"
    inactive="inactive"

class Service(Base):
    __tablename__="services"
    id=Column(Integer,primary_key=True,index=True)

    vendor_id=Column(Integer,ForeignKey("vendors.id"))
    vendor=relationship("Vendor",back_populates="vendor")

    name=Column(String,index=True)
    price_base=Column(DECIMAL,defualt=0.00)
    status=Column(Enum(Status))

    image = Column(String, nullable=True, default="default_avatar.png")
