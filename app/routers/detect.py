from fastapi import APIRouter, UploadFile, File, BackgroundTasks
import shutil
import os

router = APIRouter(prefix="/detect", tags=["Detection"])

UPLOAD_DIR = "uploaded_files"
os.makedirs(UPLOAD_DIR, exist_ok=True)  # Ensure the directory exists

@router.post("/")
async def detect(video: UploadFile = File(...), background_tasks: BackgroundTasks = None):
    # Save the uploaded video to a temporary directory
    video_path = os.path.join(UPLOAD_DIR, video.filename)
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # Add task for processing video
    if background_tasks:
        background_tasks.add_task(process_video, video_path)

    return {"message": "Video uploaded successfully and processing started!", "video_path": video_path}

def process_video(video_path: str):
    # Placeholder for video processing logic
    print(f"Processing video: {video_path}")
    # Integrate your model here
