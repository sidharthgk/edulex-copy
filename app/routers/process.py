from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.models import SessionLocal
from app.db.crud import get_queued_tasks, update_task_status
from app.services.video_processing import process_video_for_dyslexia

router = APIRouter(prefix="/process", tags=["Task Processing"])

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
async def process_tasks(db: Session = Depends(get_db)):
    """
    Process all tasks in the 'queued' state.
    """
    tasks = get_queued_tasks(db)  # Fetch only queued tasks
    results = {}

    for task in tasks:
        try:
            # Mark task as processing
            update_task_status(db, task.id, "processing")

            # Process the video (eye-tracking logic)
            result = process_video_for_dyslexia(task.video_path)

            # Mark task as completed with results
            update_task_status(db, task.id, "completed", result=str(result))
            results[task.id] = "completed"
        except Exception as e:
            # Mark task as failed with error details
            update_task_status(db, task.id, "failed", result=str(e))
            results[task.id] = f"failed: {str(e)}"

    return {"message": "Processing completed.", "results": results}
