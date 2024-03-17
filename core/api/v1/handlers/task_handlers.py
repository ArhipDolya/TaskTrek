from fastapi import APIRouter, Depends

from core.entities.task_entity import TaskEntity, TaskCreate
from core.services.task_service import TaskService
from core.api.v1.dependencies import get_task_service


router = APIRouter(prefix='/api/v1')


@router.post('/tasks/', response_model=TaskEntity)
async def create_task(task: TaskCreate, task_service: TaskService = Depends(get_task_service)):
    created_task = await task_service.create_task(task=task)
    return created_task