from fastapi import APIRouter, Depends
from app.controllers.auth_controller import register_user, login_user
from app.schemas.auth_schema import UserCreate, UserLogin
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/auth")

@router.post("/register")
def user_register(user: UserCreate):
    
    return register_user(user)


@router.post("/login")
def user_login(user: UserLogin):

    return login_user(user)


# aca estamos probando JWT
@router.get("/me")
def me(current_user = Depends(get_current_user)):

    return current_user

