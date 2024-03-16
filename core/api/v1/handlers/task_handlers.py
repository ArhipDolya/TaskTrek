from fastapi import APIRouter, Depends

from core.entities.task_entity import TaskEntity
from core.services.task_service import TaskService
from core.repositories.task_repository import SQLTaskRepository
from core.app.database import SessionLocal


router = APIRouter(prefix='/api/v1')


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
    
def get_task_service(db_session=Depends(get_db_session)):
    task_repository = SQLTaskRepository(db_session=db_session)
    return TaskService(task_repository=task_repository)


@router.post('/tasks/', response_model=TaskEntity)
async def create_task(task: TaskEntity, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task=task)