from fastapi import FastAPI
from db import add_message, get_messages

app = FastAPI()

@app.post("/messages")
def post_message(msg: dict):
    add_message(msg)
    return {"status": "ok"}

@app.get("/messages")
def list_messages():
    return get_messages()
