from fastapi import APIRouter
from app.services.queue_handler import get_queued_tasks

router = APIRouter(prefix="/queue", tags=["Queue Management"])

@router.get("/")
async def list_queues():
    """
    List all queued tasks for each user.
    """
    queues = get_queued_tasks()
    return {"queues": queues}
