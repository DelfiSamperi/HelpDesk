from app.queries.auth_queries import insert_user, fetch_user_by_email
from app.utils.auth import (
    hash_password,
    verify_password,
    create_access_token
)

def register_user(user):

    hashed_password = hash_password(user.password)

    new_user = insert_user(
        user.user_name,
        user.email,
        hashed_password
    )

    return {
        "ok": True,
        "data": new_user
    }


def login_user(user):

    existing_user = fetch_user_by_email(user.email)

    if not existing_user:

        return {
            "ok": False,
            "message": "Invalid credentials"
        }
    
    password_match = verify_password(
        user.password,
        existing_user["password_hash"]
    )

    if not password_match:

        return {
            "ok": False,
            "message": "Invalid credentials"
        }
    
    token = create_access_token({
        "sub": str(existing_user["id"]),
        "role": existing_user["user_role"]
    })
    
    return {
        "ok": True,
        "access_token": token,
        "token_type": "bearer",
        "user": {
            "id": str(existing_user["id"]),
            "user_name": existing_user["user_name"],
            "email": existing_user["email"],
            "role": existing_user["user_role"]
        }
    }

