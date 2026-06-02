from sqlalchemy import Column, Integer, String, ForeignKey, Text, CheckConstraint, DateTime
from sqlalchemy.orm import relationship
import datetime
from app.core.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True)
   
   
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    
    service_id = Column(Integer, ForeignKey("services.id"), nullable=False)
    
    
    rating = Column(Integer, nullable=False)
    
    comment = Column(Text, nullable=True)
    
    
  

  
    user = relationship("User", back_populates="reviews")
    service = relationship("Service", back_populates="reviews")


    created_at = Column(DateTime, default=datetime.datetime.utcnow)

    updated_at = Column(DateTime, default=datetime.datetime.utcnow)
   
    __table_args__ = (
        CheckConstraint('rating >= 1 AND rating <= 5', name='check_rating_range'),
    )

# تأكد من إضافة 'reviews' في كلاس User و Service
# في كلاس User: reviews = relationship("Review", back_populates="user")
# في كلاس Service: reviews = relationship("Review", back_populates="service")