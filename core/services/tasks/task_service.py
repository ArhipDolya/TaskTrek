from core.entities.tasks.task_entity import TaskEntity, TaskCreate, TaskUpdate
from core.repositories.tasks.task_repository import ITaskRepository
from core.exceptions.tasks.task_exceptions import TaskDeletionFailedException, TaskNotFoundException, TaskCreationFailedException, TaskUpdateFailedException, GetAllTasksException


class TaskService:
    
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository
        
    async def create_task(self, task: TaskCreate) -> TaskEntity:
        try:
            return await self.task_repository.create(task)
        except Exception as e:
            raise TaskCreationFailedException(reason=str(e))
    
    async def get_task_by_id(self, task_id: int) -> TaskEntity:
        task = await self.task_repository.get_by_id(task_id)
        if task is None:
            raise TaskNotFoundException(task_id=task_id)
        return task
        
    async def get_all_tasks(self) -> list[TaskEntity]:
        try:
            return await self.task_repository.get_all()
        except Exception as e:
            raise GetAllTasksException(reason=str(e))
    
    async def update_task(self, task_id: int, task: TaskUpdate) -> TaskEntity:
        try:
            updated_task = await self.task_repository.update(task_id, task)
            return updated_task
        except Exception as e:
            raise TaskUpdateFailedException(task_id=task_id, reason=str(e))
        
    async def delete(self, task_id: int) -> None:
        try:
            await self.task_repository.delete(task_id)
        except Exception as e:
            raise TaskDeletionFailedException(task_id=task_id, reason=str(e))