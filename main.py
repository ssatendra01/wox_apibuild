from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class EchoModel(BaseModel):
    text: str

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Code Engine!"}

@app.post("/echo")
def echo(data: EchoModel):
    return {"you_sent": data.text}
