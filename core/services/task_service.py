from core.entities.task_entity import TaskEntity, TaskCreate, TaskUpdate
from core.repositories.task_repository import ITaskRepository


class TaskService:
    
    def __init__(self, task_repository: ITaskRepository):
        self.task_repository = task_repository
        
    async def create_task(self, task: TaskCreate) -> TaskEntity:
        return await self.task_repository.create(task)
    
    async def get_task_by_id(self, task_id: int) -> TaskEntity:
        return await self.task_repository.get_by_id(task_id)
    
    async def get_all_tasks(self) -> list[TaskEntity]:
        return await self.task_repository.get_all()
    
    async def update_task(self, task_id: int, task: TaskUpdate) -> TaskEntity:
        return await self.task_repository.update(task_id, task)
    
    async def delete(self, task_id: int) -> None:
        return await self.task_repository.delete(task_id)