from fastapi import APIRouter, Depends
from app.controllers.auth_controller import register_user, login_user
from app.schemas.auth_schema import UserCreate, UserLogin
from app.utils.dependencies import get_current_user, require_role


router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)

@router.post(
    "/register",
    summary="User registration",
    description="""
    Creates a new user account.

    - New users are assigned the 'user' role by default.
    - User roles can only be changed by administrators.
    - Passwords are securely hashed before storage.
    - Duplicate email addresses are not allowed.
    """    
)
def user_register(user: UserCreate):
    
    return register_user(user)


@router.post(
    "/login",
    summary="User authentication",
    description="""
    Autenticates user throw email and password.

    Returns a JWT access token that must be included in the Authorization header for protected routes.
    """    
)
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


