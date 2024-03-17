from fastapi import APIRouter, Depends, HTTPException

from core.entities.task_entity import TaskEntity, TaskCreate, TaskUpdate
from core.services.task_service import TaskService
from core.exceptions.task_exceptions import GetAllTasksException, TaskNotFoundException, TaskCreationFailedException, TaskNotFoundException, TaskUpdateFailedException, TaskDeletionFailedException

from core.api.v1.dependencies import get_task_service


router = APIRouter(prefix='/api/v1')


@router.post('/tasks/', response_model=TaskEntity)
async def create_task(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    try:
        created_task = await task_service.create_task(task=task)
        return created_task
    except TaskCreationFailedException as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get('/tasks/{task_id}', response_model=TaskEntity)
async def get_task_by_id(task_id: int, task_service: TaskService = Depends(get_task_service)):
    try:
        task = await task_service.get_task_by_id(task_id=task_id)
        return task
    except TaskNotFoundException as e:
        raise HTTPException(status_code=404, detail=str(e))
    
@router.get('/tasks/', response_model=list[TaskEntity])
async def get_all_tasks(task_service: TaskService = Depends(get_task_service)):
    try:
        tasks = await task_service.get_all_tasks()
        return tasks
    except GetAllTasksException as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.put('/tasks/{task_id}', response_model=TaskEntity)
async def update_task(task_id: int, task_update: TaskUpdate, task_service: TaskService = Depends(get_task_service)):
    try:
        updated_task = await task_service.update_task(task_id=task_id, task=task_update)
        return updated_task
    except TaskUpdateFailedException as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.delete('/tasks/{task_id}', status_code=204)
async def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    try:
        await task_service.delete(task_id=task_id)
    except TaskDeletionFailedException as e:
        raise HTTPException(status_code=400, detail=str(e))