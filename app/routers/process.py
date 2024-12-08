from fastapi import APIRouter
from app.services.queue_handler import process_user_queue
from app.services.video_processing import process_video_for_dyslexia
import os

router = APIRouter(prefix="/process", tags=["Task Processing"])

@router.post("/")
async def process_tasks():
    """
    Process queued tasks for all users.
    """
    # Iterate through user queues and process tasks
    from app.services.queue_handler import user_queues

    results = {}
    for user_id, queue in user_queues.items():
        while not queue.empty():
            task = queue.get()
            try:
                result = task()  # Process the task
                results[user_id] = result  # Collect results for each user
            except Exception as e:
                results[user_id] = {"error": str(e)}

    return {"message": "Task processing completed.", "results": results}
