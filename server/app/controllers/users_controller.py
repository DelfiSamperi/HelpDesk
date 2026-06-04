from fastapi import HTTPException
import math
from app.queries.users_queries import (
    update_user_role,
    fetch_all_users,
    fetch_user_by_id,
    count_users
)

def change_user_role(user_id, role):

    role_updated = update_user_role(user_id, role)

    return {
        "ok": True,
        "data": role_updated
    }


def all_users(page, limit):

    offset = (page - 1) * limit

    users = fetch_all_users(limit, offset)

    total_users = count_users()

    total_pages = math.ceil(total_users / limit)

    return {
        "ok": True,
        "page": page,
        "limit": limit,
        "total_users": total_users,
        "total_pages": total_pages,
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