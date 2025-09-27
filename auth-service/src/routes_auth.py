from fastapi import APIRouter

router = APIRouter()

# Health check endpoint
@router.get("/health")
def health():
    return {"status": "ok"}

# Existing login route
from pydantic import BaseModel
from fastapi import HTTPException

class UserLogin(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(user: UserLogin):
    # Simple dummy authentication
    if user.username == "admin" and user.password == "password":
        return {"token": "fake-jwt-token"}
    raise HTTPException(status_code=401, detail="Invalid credentials")
