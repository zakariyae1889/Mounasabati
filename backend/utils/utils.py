import uuid
from slugify import slugify
from models.service import Service
from dotenv import load_dotenv
import os

from datetime import datetime,timedelta,timezone
from typing import Optional
from passlib.context import CryptContext
from jose import jwt


load_dotenv()

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORITHM=os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES=int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


def hash_password(password:str)->str:
    return pwd_context.hash(password)

def verify_password(plain_password:str,hashed_password:str)->bool:
    return pwd_context.verify(plain_password,hashed_password)


def create_access_token(data:dict,expires_delta:Optional[timedelta]=None)->str:
    to_encode=data.copy()
    if expires_delta:
        expire=datetime.now(timezone.utc)+expires_delta
    else:
        expire=datetime.now(timezone.utc)+timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp":expire})
    encoded_jwt=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt





def generate_uinque_slug(db,service_name:str)->str:
    slug=slugify(service_name)
    while db.query(Service).filter(Service.slug==slug).first():
        slug=slugify(service_name)+"-"+str(uuid.uuid4())[:8]
    return slug


