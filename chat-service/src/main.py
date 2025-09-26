from fastapi import FastAPI, WebSocket
from ws_handlers import websocket_endpoint

app = FastAPI()

@app.websocket("/ws")
async def websocket_route(websocket: WebSocket):
    await websocket_endpoint(websocket)
