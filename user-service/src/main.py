from fastapi import FastAPI
from routes_user import router

app = FastAPI()
app.include_router(router)
