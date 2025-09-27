# main.py
from fastapi import FastAPI
from analytics import record_event, get_events

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/events")
def post_event(event: dict):
    record_event(event)
    return {"status": "ok"}

@app.get("/events")
def list_events():
    return get_events()
