from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# For registration
class UserRegister(BaseModel):
    username: str
    password: str

# For login
class UserLogin(BaseModel):
    username: str
    password: str

# Register endpoint
@router.post("/register")
async def register(user: UserRegister):
    return {"message": f"user {user.username} registered successfully"}

# Login endpoint
@router.post("/login")
async def login(user: UserLogin):
    return {"message": f"user {user.username} logged in successfully"}

@router.post("/login")
async def login(user: UserLogin):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"token": f"fake-jwt-token-for-{user.username}"}
