from fastapi import APIRouter

router = APIRouter()
users = []

@router.post("/register")
def register_user(user: dict):
    users.append(user)
    return {"message": "User registered successfully", "user_id": len(users)-1}

@router.get("/profile")
def profile():
    if not users:
        return {"error": "No users registered"}
    return users[0]

@router.get("/")
def get_users():
    return users

@router.get("/{user_id}")
def get_user(user_id: int):
    if user_id < 0 or user_id >= len(users):
        return {"error": "User not found"}
    return users[user_id]
