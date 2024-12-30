from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException
import os
import shutil
from moviepy.video.io.VideoFileClip import VideoFileClip
from app.services.queue_handler import add_task_to_queue
from sqlalchemy.orm import Session
from fastapi import Depends
from app.db.models import SessionLocal
from app.db.crud import create_task, update_task_status


router = APIRouter(prefix="/detect", tags=["Detection"])

BASE_DIR = "app/data/uploads"
os.makedirs(BASE_DIR, exist_ok=True)  # Ensure the base directory exists


# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def detect(
    user_id: str,
    video: UploadFile = File(...),
    background_tasks: BackgroundTasks = None,
    db: Session = Depends(get_db),
):
    # Validate file type
    if not video.content_type.startswith("video/"):
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a video file.")

    # Create user directory
    user_dir = os.path.join(BASE_DIR, user_id)
    os.makedirs(user_dir, exist_ok=True)

    # Save the video to the user's directory
    video_path = os.path.join(user_dir, video.filename)
    with open(video_path, "wb") as buffer:
        shutil.copyfileobj(video.file, buffer)

    # Extract audio and store in the same directory
    audio_path = os.path.splitext(video_path)[0] + ".wav"
    extract_audio(video_path, audio_path)

    # Save the task to the database
    task = create_task(db=db, user_id=user_id, video_path=video_path, audio_path=audio_path)

    # Add task for processing video
    if background_tasks:
        background_tasks.add_task(process_video, user_id, video_path, audio_path)

    return {
        "message": "Video uploaded successfully, audio extracted, and processing started!",
        "user_id": user_id,
        "video_path": video_path,
        "audio_path": audio_path,
    }

def extract_audio(video_path: str, audio_path: str):
    try:
        video = VideoFileClip(video_path)

        # Check if the video contains an audio track
        if video.audio is None:
            raise ValueError("The uploaded video does not contain an audio track.")

        # Extract and save the audio
        video.audio.write_audiofile(audio_path)
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error extracting audio: {str(e)}")


def process_video(user_id: str, video_path: str, audio_path: str):
    # Placeholder for video processing logic
    print(f"Processing video for user {user_id}: {video_path}")
    print(f"Processing audio for user {user_id}: {audio_path}")
    # Your video and audio processing logic goes here
