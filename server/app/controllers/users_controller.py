from fastapi import HTTPException
from app.queries.users_queries import (
    update_user_role,
    fetch_all_users,
    fetch_user_by_id
)

def change_user_role(user_id, role):

    role_updated = update_user_role(user_id, role)

    return {
        "ok": True,
        "data": role_updated
    }


def all_users():

    users = fetch_all_users()

    return {
        "ok": True,
        "data": users
    }


def user_by_id(id):

    user_id = fetch_user_by_id(id)

    if not user_id:

        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
    
    return {
        "ok": True,
        "data": user_id
    }