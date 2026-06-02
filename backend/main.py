import uvicorn
from app.core.database import engine
from app import models
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
if __name__=="__main__":
   models.Base.metadata.create_all(bind=engine)
   uvicorn.run("app.app:app",host="127.0.0.1",port=8000,reload=True)