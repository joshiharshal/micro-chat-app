from fastapi import FastAPI

app = FastAPI()

def send_notification(message: str):
    print(f"Notification: {message}")

@app.post("/notify/")
def notify(msg: dict):
    send_notification(msg.get("message", ""))
    return {"status": "sent"}

@app.get("/health")
def health():
    return {"status": "ok"}
