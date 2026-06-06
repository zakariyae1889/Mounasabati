from pydantic import BaseModel ,EmailStr,Field
from typing import Optional
from uuid import UUID
class UserCreate(BaseModel):
    username: str = Field(..., min_length=4, max_length=16)
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    CIN: str = Field(..., pattern=r"^[A-Z,a-z]{1,2}\d{5,7}$")
    password: str = Field(..., min_length=8, max_length=100)
    role: Optional[str] = "client"
    image_profile: Optional[str] = None



class UserOut(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    first_name: Optional[str]
    last_name: Optional[str]
    CIN: str
    role: str

    class Config: 
        from_attributes = True


class UserUpdate(BaseModel):
    Username:Optional[str]=None
    Email:Optional[EmailStr]=None
    First_name:Optional[str]=None
    Last_name:Optional[str]=None
   
 
class UserLgoin(BaseModel):
   Username:str=Field(...,min_length=4,max_length=16)
   Password:str=Field(...,min_length=8,max_length=16)