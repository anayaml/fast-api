from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/')
def read_root():
    return {'Hello' : 'world'}

@app.get('/itens/{id}')
def read_item(id: int, q: Union[str, None] = None):
    return {'id': id, 'q': q}

@app.put('/itens/{id}')
def update_item(id: int, item: Item):
    return {'name': item.name, 'id': id}