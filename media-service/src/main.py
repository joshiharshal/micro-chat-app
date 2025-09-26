from fastapi import FastAPI
from media_routes import router

app = FastAPI()
app.include_router(router)
