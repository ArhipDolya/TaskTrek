from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Task(BaseModel):
    id: int
    title: str
    description: str
    status: str = Field(default='Not completed')
    due_date: Optional[datetime] = None
    
