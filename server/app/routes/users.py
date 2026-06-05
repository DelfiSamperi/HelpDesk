from fastapi import APIRouter, Depends
from app.schemas.user_schema import UserRoleUpdate
from app.controllers.users_controller import (
    change_user_role,
    all_users,
    user_by_id
)
from app.utils.dependencies import require_role


router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# ruta cambio de rol
@router.patch(
    "/{user_id}/role",
    summary="Change user role",
    description="""
    Users are registered with default role 'user'.
    Administrators can change users' roles.
    """
)
def change_role(
    user_id: str,
    role_data: UserRoleUpdate,
    current_user = Depends(require_role(["admin"]))
):
    return change_user_role(user_id, role_data.role)


@router.get(
    "/",
    summary="Get list of all users",
    description="""
    Administrators can access to a paginated list of all users.

    Available information:
    - ID
    - Name
    - Email
    - Role
    - Active
    - Created at
    """    
)
def get_users(
    page: int = 1,
    limit: int= 12,
    current_user = Depends(require_role(["admin"]))
):

    return all_users(page, limit)


@router.get(
    "/{id}",
    summary="Get one user by id",
    description="Administrator can access to one user info."    
)
def get_user_by_id(
    id: str,
    current_user = Depends(require_role(["admin"]))
):

    return user_by_id(id)

