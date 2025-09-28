from fastapi import FastAPI, WebSocket
from ws_handlers import websocket_endpoint
from routes_chat import router as chat_router

app = FastAPI()

# Mount REST endpoints **without prefix** (matches nginx /chat/)
app.include_router(chat_router)

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)

@app.get("/health")
def health():
    return {"status": "ok"}
