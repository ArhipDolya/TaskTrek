from abc import ABC, abstractmethod
from typing import Optional

from sqlalchemy.orm import Session

from core.entities.task_entity import TaskEntity, TaskCreate, TaskUpdate
from core.models.task_model import TaskModel


class ITaskRepository(ABC):
    
    @abstractmethod
    async def create(self, task: TaskCreate) -> TaskEntity:
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
        
    async def create(self, task: TaskCreate) -> TaskEntity:
        db_task = TaskModel(**task.dict())
        self.db_session.add(db_task)
        self.db_session.commit()
        self.db_session.refresh(db_task)
        
        return TaskEntity.from_orm(db_task)
        
    async def get_by_id(self, id: int) -> Optional[TaskEntity]:
        db_task = self.db_session.query(TaskModel).filter(TaskModel.id == id).first()
        if db_task:
            return TaskEntity.from_orm(db_task)
        return None
        
    async def get_all(self) -> list[TaskEntity]:
        db_tasks = self.db_session.query(TaskModel).all()
        return [TaskEntity.from_orm(task) for task in db_tasks]
        
    async def update(self, task_id: int, task: TaskUpdate) -> TaskEntity:
        db_task = self.db_session.query(TaskModel).filter(TaskModel.id == task_id).first()
        if db_task:
            task_data = task.dict(exclude_unset=True)
            for key, value in task_data.items():
                setattr(db_task, key, value)
            self.db_session.commit()
            return TaskEntity.from_orm(db_task)
        return None

    async def delete(self, task_id: int) -> None:
        db_task = self.db_session.query(TaskModel).filter(TaskModel.id == task_id).first()
        self.db_session.delete(db_task)
        self.db_session.commit()