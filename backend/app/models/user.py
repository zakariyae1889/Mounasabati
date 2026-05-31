from sqlalchemy import Column,Integer,String,Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
import enum


class UserRole(enum.Enum):
    client="client"
    vendor="vendor"


class User(Base):
    __tablename__="users"
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String,unique=True,index=True)
    first_name=Column(String,index=True,nullable=True)
    last_name=Column(String,index=True,nullable=True)
    email=Column(String,unique=True,index=True)
    CIN=Column(String,unique=True,index=True)
    role=Column(Enum(UserRole),defualt=UserRole.client)
    password=Column(String)

    client=relationship("Client",back_populates="user")
    vendor=relationship("Vendor",back_populates="user")




