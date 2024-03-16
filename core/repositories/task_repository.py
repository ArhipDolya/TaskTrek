from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from core.entities.task_entity import TaskEntity
from core.models.task_model import TaskModel


class ITaskRepository(ABC):
    
    @abstractmethod
    async def create(self, task: TaskEntity) -> TaskEntity:
        ...
        
    @abstractmethod
    async def get_by_id(self, id: int) -> Optional[TaskEntity]:
        ...
        
    @abstractmethod
    async def get_all(self) -> list[TaskEntity]:
        ...
        
    @abstractmethod
    async def update(self, task_id: int, task: TaskEntity) -> TaskEntity:
        ...
        
    @abstractmethod
    async def delete(self, task_id: int) -> None:
        ...


class SQLTaskRepository(ITaskRepository):
    
    def __init__(self, db_session: Session):
        self.db_session = db_session
        
    async def create(self, task: TaskEntity) -> TaskEntity:
        db_task = TaskModel(**task.dict())
        print(db_task)
        self.db_session.add(db_task)
        self.db_session.commit()
        self.db_session.refresh(db_task)

        return TaskEntity.model_validate(db_task)
        
    async def get_by_id(self, id: int) -> Optional[TaskEntity]:
        ...
        
    async def get_all(self) -> list[TaskEntity]:
        ...
        
    async def update(self, task_id: int, task: TaskEntity) -> TaskEntity:
        ...
        
    async def delete(self, task_id: int) -> None:
        ...