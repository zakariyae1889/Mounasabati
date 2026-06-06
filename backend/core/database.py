from sqlmodel import create_engine, Session, SQLModel

from models.client import Client
from models.user import User
from models.vendor import Vendor
from models.service import Service
from models.booking import Booking  
from models.reviews import Review
from models.payment import Payment
from models.notification import Notification


# مسار مباشر وصريح وقصير جداً
DATABASE_URL = "sqlite:///mounasabati.sqlite"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():
   
    SQLModel.metadata.create_all(engine)

   



def get_session():
    with Session(engine) as session:
        yield session