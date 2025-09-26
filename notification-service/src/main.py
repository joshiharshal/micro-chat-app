from fastapi import FastAPI
from notifier import send_notification

app = FastAPI()

@app.post("/notify")
def notify(msg: dict):
    send_notification(msg.get("message", ""))
    return {"status": "sent"}
