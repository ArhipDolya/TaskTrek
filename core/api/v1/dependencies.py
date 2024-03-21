from fastapi import Depends

from sqlalchemy.orm import Session

from core.services.tasks.task_service import TaskService
from core.repositories.tasks.task_repository import SQLTaskRepository
from core.app.database import SessionLocal


def get_db_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_task_service(db_session: Session = Depends(get_db_session)):
    task_repository = SQLTaskRepository(db_session=db_session)
    return TaskService(task_repository=task_repository)