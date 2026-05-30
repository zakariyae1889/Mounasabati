from fastapi import FastAPI

app = FastAPI()  # يجب أن يكون الاسم 'app'

@app.get("/")
def read_root():
    return {"Hello": "World"}