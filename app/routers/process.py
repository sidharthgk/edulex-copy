from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.crud import update_task_status, get_all_tasks as get_queued_tasks
from app.db.models import SessionLocal
from app.services.video_processing import process_video_for_dyslexia

router = APIRouter(prefix="/process", tags=["Task Processing"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def process_tasks(db: Session = Depends(get_db)):
    tasks = get_queued_tasks(db)
    results = {}

    for task in tasks:
        try:
            # Mark task as processing
            update_task_status(db, task.id, "processing")

            # Process the video
            result = process_video_for_dyslexia(task.video_path)

            # Mark task as completed
            update_task_status(db, task.id, "completed", result=str(result))
            results[task.id] = "completed"
        except Exception as e:
            # Mark task as failed
            update_task_status(db, task.id, "failed", result=str(e))
            results[task.id] = f"failed: {str(e)}"

    return {"message": "Processing completed.", "results": results}
