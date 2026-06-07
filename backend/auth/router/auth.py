from fastapi import APIRouter,Depends,HTTPException,status
from sqlmodel import Session,select
from core.database import get_session
