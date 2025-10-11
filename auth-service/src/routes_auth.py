from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class UserRegister(BaseModel):
    username: str
    password: str

@router.post("/register")
async def register(user: UserRegister):
    # dummy response for now
    return {"message": f"user {user.username} registered successfully"}

@router.post("/login")
async def login(user: UserLogin):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"token": f"fake-jwt-token-for-{user.username}"}