from pydantic import BaseModel
from uuid import UUID


class CommentCreate(BaseModel):
    created_by: UUID
    message: str

