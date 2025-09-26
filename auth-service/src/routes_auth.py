from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: UserLogin):
    # Simple dummy authentication
    if user.username == "admin" and user.password == "password":
        return {"token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
