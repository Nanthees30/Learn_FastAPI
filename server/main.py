from fastapi import FastAPI, Body, Form
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    in_stock: bool

@app.post("/json")
def receive_json(item: Item):
    return {
        "type": "JSON",
        "name": item.name,
        "price": item.price,
        "in_stock": item.in_stock
    }

@app.post("/text")
def receive_text(content: str = Body(None, media_type="text/plain")):
    return {
        "type": "Plain text",
        "content": content
    }

@app.post("/form")
def receive_form(username: str = Form(...), password: str = Form(...)):
    return {
        "type": "Form Data",
        "username": username,
        "password": password
    }