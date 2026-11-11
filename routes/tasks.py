from fastapi import APIRouter, HTTPException
from schema.schemas import TaskCreate, TaskUpdate
from service import models

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# CREATE TASK
@router.post("/")
def create_new_task(task: TaskCreate):
    task_id = models.create_task(task)

    return {
        "message": "Task created successfully",
        "id": task_id
    }


# GET ALL TASKS
@router.get("/")
def get_all_tasks():
    tasks = models.get_all_task()
    return tasks


# GET TASK BY ID
@router.get("/{task_id}")
def get_id(task_id: int):
    task = models.get_task_by_id(task_id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    return task


# UPDATE TASK
@router.put("/{task_id}")
def update_data(task_id: int, task_data: TaskUpdate):
    updated = models.update_task(task_id, task_data)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    return {"message": "Task updated successfully"}


# DELETE TASK
@router.delete("/{task_id}")
def delete_task(task_id: int):
    deleted = models.delete_id(task_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Task Not Found"
        )

    return {"message": "Task deleted successfully"}