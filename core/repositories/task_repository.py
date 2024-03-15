from abc import ABC, abstractmethod
from typing import Optional

from core.domain.entities.task import TaskEntity


class ITaskRepository(ABC):
    
    @abstractmethod
    async def add(self, task: TaskEntity) -> TaskEntity:
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

