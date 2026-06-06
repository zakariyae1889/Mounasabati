from pydantic import BaseModel,Field
from datetime import date, time
from uuid import UUID
from schemas.service import ServiceOut
from models.booking import BookingStatus


class BookingCreate(BaseModel):
    service_id: UUID
    event_date: date
    event_time: time 
    total_price: float = Field(..., gt=0)

class BookingReceipt(BaseModel):
    id: UUID
    event_date: date
    total_price: float
    status:BookingStatus
    service: ServiceOut # يعطيك تفاصيل الخدمة المحجوزة
    message: str = "تم تأكيد حجزك بنجاح! شكراً لاختيارك مناسبتي."

    class Config:
        from_attributes = True