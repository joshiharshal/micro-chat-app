from fastapi import FastAPI
from routes_group import router

app = FastAPI()
app.include_router(router)
