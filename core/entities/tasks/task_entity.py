from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class TaskEntity(BaseModel):
    id: int
    title: str
    description: str
    status: str = Field(default='Not completed')
    due_date: Optional[datetime] = None
    
    class Config:
        from_attributes = True

class TaskCreate(BaseModel):
    title: str
    description: str
    status: str = Field(default='Not completed')
    due_date: Optional[datetime] = None
    
class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    due_date: Optional[datetime] = None