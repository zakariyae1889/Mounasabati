from fastapi import FastAPI
from core.database import init_db
import uvicorn

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield

app = FastAPI(lifespan=lifespan)


@app.get("/")
def hello_word():
        return {"message":"Hello World"}



if __name__=="__main__":
    init_db()
    uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)