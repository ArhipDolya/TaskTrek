from http.client import HTTPException
from fastapi import APIRouter, Depends

from core.entities.task_entity import TaskEntity, TaskCreate, TaskUpdate
from core.services.task_service import TaskService
from core.api.v1.dependencies import get_task_service


router = APIRouter(prefix='/api/v1')


@router.post('/tasks/', response_model=TaskEntity)
async def create_task(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    created_task = await task_service.create_task(task=task)
    return created_task

@router.get('/tasks/{task_id}', response_model=TaskEntity)
async def get_task_by_id(task_id: int, task_service: TaskService = Depends(get_task_service)):
    task = await task_service.get_task_by_id(task_id=task_id)
    return task

@router.get('/tasks/', response_model=list[TaskEntity])
async def get_all_tasks(task_service: TaskService = Depends(get_task_service)):
    tasks = await task_service.get_all_tasks()
    return tasks

@router.put('/tasks/{task_id}', response_model=TaskEntity)
async def update_task(task_id: int, task_update: TaskUpdate, task_service: TaskService = Depends(get_task_service)):
    updated_task = await task_service.update_task(task_id=task_id, task=task_update)
    if updated_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task
    
@router.delete('/tasks/{task_id}', status_code=204)
async def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    deleted_task = await task_service.delete(task_id=task_id)
    return deleted_task