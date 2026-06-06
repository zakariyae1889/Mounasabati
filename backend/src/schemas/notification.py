from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from src.schemas.user import UserOut

class NotificationCreate(BaseModel):
   
    title: str
    body: str


class NotificationUpdate(BaseModel):
    is_read: bool

class NotificationRead(BaseModel):
    id: UUID
    user:UserOut
    title: str
    body: str
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True 
