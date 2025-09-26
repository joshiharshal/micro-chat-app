from fastapi import APIRouter

router = APIRouter()
groups = []

@router.post("/groups")
def create_group(group: dict):
    groups.append(group)
    return {"message": "Group created"}

@router.get("/groups")
def list_groups():
    return groups
