# routes_user.py
from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel

router = APIRouter()

# Fake in-memory user database
users_db = {
    "harshal": {"username": "harshal", "password": "1234", "email": "harshal@example.com"},
    "alice": {"username": "alice", "password": "pass", "email": "alice@example.com"}
}

# Simple token store (username -> token)
tokens = {}

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(req: LoginRequest):
    user = users_db.get(req.username)
    if not user or user["password"] != req.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    # Simple token generation (just for demo)
    token = f"token-{req.username}"
    tokens[token] = req.username
    return {"access_token": token, "token_type": "bearer"}

# Profile endpoint
@router.get("/profile")
def profile(authorization: str = Header(None)):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing token")
    
    token = authorization.split(" ")[1]
    username = tokens.get(token)
    if not username:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    user = users_db[username]
    return {"username": user["username"], "email": user["email"]}
