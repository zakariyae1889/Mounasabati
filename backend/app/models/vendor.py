from sqlalchemy import Column,Integer,String,ForeignKey,Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class Vendor(Base):
    __tablename__="vendors"
    id=Column(Integer,primary_key=True,index=True)

    user_id=Column(Integer,ForeignKey("users.id"))
    


    business_name=Column("String",index=True)

    phone=Column(String,index=True)
    city=Column(String,index=True)
    
    rc_number=Column(String,index=True)
    address=Column(String,index=True)
    description=Column(Text,nullable=True)

    user=relationship("User",back_populates="vendor")
    vendor=relationship("Service",back_populate="service")
