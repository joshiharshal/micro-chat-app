from fastapi import APIRouter

router = APIRouter()

users = []

@router.post("/register")
def register_user(user: dict):
    users.append(user)
    return {"message": "User registered successfully"}

@router.get("/users")
def get_users():
    return users
