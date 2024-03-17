from sqlalchemy import Column, Integer, String, DateTime

from core.app.database import Base


class TaskModel(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, default="Not completed")
    due_date = Column(DateTime, nullable=True)