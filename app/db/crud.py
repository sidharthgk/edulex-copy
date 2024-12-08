from sqlalchemy.orm import Session
from app.db.models import Task

def create_task(db: Session, user_id: str, video_path: str, audio_path: str):
    """Add a new task to the database."""
    task = Task(user_id=user_id, video_path=video_path, audio_path=audio_path, status="queued")
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def update_task_status(db: Session, task_id: int, status: str, result: str = None):
    """Update the status and result of a task."""
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.status = status
        task.result = result
        db.commit()
        db.refresh(task)
    return task

def get_all_tasks(db: Session):
    """Retrieve all tasks."""
    return db.query(Task).all()
