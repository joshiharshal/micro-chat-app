from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncpg
import hashlib

router = APIRouter()

DB_USER = "chat_user"
DB_PASS = "chat_pass"
DB_NAME = "chat_db"
DB_HOST = "postgres"

class UserRegister(BaseModel):
    username: str
    password: str

def hash_password(password: str):
    return hashlib.sha256(password.encode()).hexdigest()

@router.post("/register")
async def register(user: UserRegister):
    try:
        conn = await asyncpg.connect(
            user=DB_USER, password=DB_PASS, database=DB_NAME, host=DB_HOST
        )
        existing = await conn.fetchrow(
            "SELECT * FROM users WHERE username=$1", user.username
        )
        if existing:
            await conn.close()
            raise HTTPException(status_code=400, detail="Username already exists")

        await conn.execute(
            "INSERT INTO users(username, password) VALUES($1, $2)",
            user.username, hash_password(user.password)
        )
        await conn.close()
        return {"message": "Registration successful!"}

    except Exception as e:
        print("DB Error:", e)
        raise HTTPException(status_code=500, detail="Server error")

@router.post("/login")
async def login(user: UserRegister):
    try:
        conn = await asyncpg.connect(
            user=DB_USER, password=DB_PASS, database=DB_NAME, host=DB_HOST
        )
        existing = await conn.fetchrow(
            "SELECT * FROM users WHERE username=$1", user.username
        )
        await conn.close()

        if existing and existing["password"] == hash_password(user.password):
            return {"token": "fake-jwt-token"}

        raise HTTPException(status_code=401, detail="Invalid credentials")

    except Exception as e:
        print("DB Error:", e)
        raise HTTPException(status_code=500, detail="Server error")
