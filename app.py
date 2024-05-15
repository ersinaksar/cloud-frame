from fastapi import FastAPI
from pydantic import BaseModel
import solara.server.fastapi

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str


@app.get("/api/data")
def read_data():
    return {"message": "Hello, this is your SaaS application!"}


@app.post("/api/items")
def create_item(item: Item):
    return item


class BirthInfo(BaseModel):
    day: str
    month: str
    year: str
    hour: str
    minute: str
    location: str


@app.post("/submit")
async def submit_birth_info(birth_info: BirthInfo):
    print(f"Received birth info: {birth_info}")
    return {"message": "Birth info received successfully", "data": birth_info}


app.mount("/", app=solara.server.fastapi.app)
