from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from fastapi import FastAPI


class Item(BaseModel):
    username: str
    timestamp: datetime

app = FastAPI()


@app.get("/api/")
def read_root():
    json_compatible_item_data = jsonable_encoder({"username": "FastAPI", 'timestamp': datetime.now()})
    return JSONResponse(content=json_compatible_item_data)
