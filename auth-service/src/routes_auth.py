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
