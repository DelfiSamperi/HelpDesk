from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from enum import Enum

class PriorityEnum(str, Enum):
    low = "low"
    medium = "medium"
    high = "high"
    urgent = "urgent"


class StatusEnum(str, Enum):
    open = 'open'
    in_progress = 'in_progress'
    resolved = 'resolved'


class TicketCreate(BaseModel):
    title: str
    description: str
    priority: PriorityEnum
    category_id: Optional[int] = None


class TicketUpdate(BaseModel):
    status: Optional[StatusEnum] = None
    priority: Optional[PriorityEnum] = None
    assigned_to: Optional[UUID] = None
    category_id: Optional[int] = None



   
    