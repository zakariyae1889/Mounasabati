from pydantic import BaseModel,Field
from typing import Optional
from datetime import date, time


class BookingCreate(BaseModel):
        Event_date:str=Field(...,min_length=4,max_length=16)
        Total_price:float
        Status:str=Field(...,pattern=r"^(pending|confirmed|paid|cancelled)$")



class BookingReceipt(BaseModel):
    booking_id: int
    service_name: str
    event_date: date
    event_time: time
    total_price: float
    Status: str
    message: str = "تم تأكيد حجزك بنجاح! شكراً لاختيارك مناسبتي."