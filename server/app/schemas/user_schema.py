from pydantic import BaseModel
from enum import Enum

class RoleEnum(str, Enum):
    user = 'user'
    tech = 'tech'
    admin = 'admin'

class UserRoleUpdate(BaseModel):
    role: RoleEnum


    