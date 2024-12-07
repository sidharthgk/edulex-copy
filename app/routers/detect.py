from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException
from typing import Optional
import os
import shutil

router = APIRouter(prefix="/detect", tags=["Detection"])

BASE_DIR = "app/data"
os.makedirs(BASE_DIR, exist_ok=True)  # Ensure the base directory exists

@router.post("/")
async def detect(
    user_id: str,
    video: UploadFile = File(...),
    background_tasks: BackgroundTasks = None,
):
    # Create user directory
    user_dir = os.path.join(BASE_DIR, user_id)
    os.makedirs(user_dir, exist_ok=True)

    # Save the video to the user's directory
    video_path = os.path.join(user_dir, video.filename)
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # Add task for processing video
    if background_tasks:
        background_tasks.add_task(process_video, user_id, video_path)

    return {
        "message": "Video uploaded successfully and processing started!",
        "user_id": user_id,
        "video_path": video_path,
    }

def process_video(user_id: str, video_path: str):
    # Placeholder for video processing logic
    print(f"Processing video for user {user_id}: {video_path}")
    # Your video processing logic goes here
