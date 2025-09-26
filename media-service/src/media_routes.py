from fastapi import APIRouter, UploadFile, File

router = APIRouter()
media_files = []

@router.post("/upload")
async def upload_media(file: UploadFile = File(...)):
    content = await file.read()
    media_files.append({"filename": file.filename, "size": len(content)})
    return {"status": "uploaded"}

@router.get("/media")
def list_media():
    return media_files
