from fastapi import APIRouter
from app.controllers.auth_controller import register_user, login_user
from app.schemas.auth_schema import UserCreate, UserLogin

router = APIRouter(prefix="/auth")

# registro de nuevo usuario
@router.post("/register")
def user_register(user: UserCreate):
    
    print("route user register")
    return register_user(user)


#login de usuarios
@router.post("/login")
def user_login(user: UserLogin):

    print("route login user")
    return login_user(user)