from fastapi import APIRouter
from app.controllers.auth_controller import register_user, login_user
from app.schemas.auth_schema import UserCreate, UserLogin

router = APIRouter(prefix="/auth")

@router.post("/register")
def user_register(user: UserCreate):
    
    return register_user(user)


@router.post("/login")
def user_login(user: UserLogin):

    return login_user(user)