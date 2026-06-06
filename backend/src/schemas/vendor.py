from pydantic import Field,BaseModel
from typing import Optional
from src.schemas.user import UserOut


class VendorCreate(BaseModel):
    business_name: str = Field(..., min_length=4, max_length=50)
    phone: str = Field(..., min_length=8, max_length=16)
    city: str = Field(..., min_length=3)
    address: str = Field(..., min_length=4)
    rc_number: str = Field(...)
    description: Optional[str] = None
    
class VendorUpdate(BaseModel):
    Business_name:Optional[str]=None
    Phone:Optional[str]=None
    City:Optional[str]=None
    Address:Optional[str]=None
    RC_number:Optional[str]=None
    Description:Optional[str]=None
    Image:Optional[str]=None

class VendorOut(BaseModel):
    business_name: str
    phone: str
    city: str
    address: str
    description: Optional[str]
    image: Optional[str]
    user: UserOut  # إذا أردت تضمين بيانات المستخدم الأساسية

    class Config:
        from_attributes = True