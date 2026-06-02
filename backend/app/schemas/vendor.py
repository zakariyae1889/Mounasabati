from pydantic import Field,BaseModel
from typing import Optional



class VendorCreate(BaseModel):
    Business_name:str=Field(...,min_length=4,max_length=16)
    Phone:str=Field(...,min_length=8,max_length=16)
    City:str=Field(...,min_length=4,max_length=16)
    Address:str=Field(...,min_length=4,max_length=16)
    RC_number:str=Field(...,min_length=4,max_length=16)
    Description:Optional[str]=None
    
class VendorUpdate(BaseModel):
    Business_name:Optional[str]=None
    Phone:Optional[str]=None
    City:Optional[str]=None
    Address:Optional[str]=None
    RC_number:Optional[str]=None
    Description:Optional[str]=None
    Image:Optional[str]=None

class VendorOut(BaseModel):
    Business_name:str
    Phone:str
    City:str
    Address:str
    RC_number:str
    Description:str
    Image:str
    
    class config:
        from_attributes=True