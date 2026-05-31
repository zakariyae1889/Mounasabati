from sqlalchemy import Column,Integer,String,ForeignKey,Text
from sqlalchemy.orm import relationship
from app.core.database import Base




class Client(Base):
    __tablename__="clients"
    id=Column(Integer,primary_key=True,index=True)
    user_id=Column(Integer,ForeignKey("users.id"))
 
    phone=Column(String,index=True)
    city=Column(String,index=True)
    address=Column(String,index=True)

    user=relationship("User",back_populates="client")
