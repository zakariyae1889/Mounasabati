from pydantic import BaseModel
from typing import Optional
from app.schemas.user import UserOut
from pydantic import BaseModel
from uuid import UUID

class ClientCrete(BaseModel):
    Phone:Optional[str]=None
    City:Optional[str]=None
    Address:Optional[str]=None
    Image:Optional[str]=None

class ClientUpdate(BaseModel):
    Phone:Optional[str]=None
    City:Optional[str]=None
    Address:Optional[str]=None
    Image:Optional[str]=None


class ClientOut(BaseModel):
    id:UUID
    user:UserOut
    Phone:str
    City:str
    Address:str
    Image:str
    
    class config:
        from_attributes=True
