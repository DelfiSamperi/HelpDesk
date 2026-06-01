from fastapi import APIRouter, Depends
from app.controllers.auth_controller import register_user, login_user
from app.schemas.auth_schema import UserCreate, UserLogin
from app.utils.dependencies import get_current_user, require_role


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post("/register")
def user_register(user: UserCreate):
    
    return register_user(user)


@router.post("/login")
def user_login(user: UserLogin):

    return login_user(user)


# RUTA DE PRUEBA JWT
@router.get("/me")
def me(current_user = Depends(get_current_user)):

    return current_user


# RUTA DE PRUEBA PARA EL ADMIN
@router.get("/admin-test")
def admin_test(
    current_user = Depends(
        require_role(["admin"])
    )
):
    
    return {
        "message": "Admin access granted"
    }


