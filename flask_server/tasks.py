import time
import celery

app = celery.Celery('tasks', broker="redis://localhost:6379", backend="redis://localhost:6379/4")

@celery.task
def my_background_task(arg1):
    time.sleep(10)
    return "Completed: " + arg1
