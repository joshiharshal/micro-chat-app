from fastapi import FastAPI
from routes_user import router

app = FastAPI()

# Mount router with /users prefix to match nginx routing
app.include_router(router, prefix="")

@app.get("/health")
def health():
    return {"status": "ok"}
