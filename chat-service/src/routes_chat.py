# routes_chat.py
from fastapi import APIRouter
import asyncio
from ws_handlers import clients  # shared list of connected websockets

router = APIRouter()
messages = []

@router.post("/send")
async def send_message(user_id: int, msg: str):
    messages.append({"user_id": user_id, "msg": msg})
    # broadcast safely
    for client in clients.copy():  # use copy to avoid modification during iteration
        try:
            await client.send_text(f"User {user_id}: {msg}")
        except:
            clients.remove(client)
    return {"status": "message sent"}

@router.get("/")
def get_messages():
    return messages
