from fastapi import APIRouter, UploadFile, File, BackgroundTasks
import shutil
import os

router = APIRouter(prefix="/detect", tags=["Detection"])

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the directory exists

@router.post("/")
async def detect(video: UploadFile = File(...), background_tasks: BackgroundTasks = None):
   pass

def process_video(video_path: str):
    # Placeholder for video processing logic
    pass
    # Integrate your model here
