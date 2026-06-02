from pydantic import BaseModel,Field
from typing import Optional



class VendorCreate(BaseModel):
    ServiceName:str=Field(...,min_length=4,max_length=16)
    Price_base:float
    Image:Optional[str]=None
    status:str=Field(...,pattern=r"^(active|inactive)$")

class VendorUpdate(BaseModel):
    ServiceName:Optional[str]=None
    Price_base:Optional[float]=None
    Image:Optional[str]=None

class VendorOut(BaseModel):
    ServiceName:str
    Price_base:float
    Image:str
    status:str
    
    class config:
        from_attributes=True