from fastapi import (
    Header,
    HTTPException,
    Depends
)

from app.utils.auth import verify_token

def get_current_user(authorization: str = Header(None)):
    
    print("Auth header:")
    print(authorization)

    if not authorization:

        raise HTTPException(
            status_code=401,
            detail="Authorization header missing"
        )
    
    try:

        scheme, token = authorization.split()

    except ValueError:

        raise HTTPException(
            status_code=401,
            detail="Invalid token format"
        )
    
    if scheme.lower() != "bearer":

        raise HTTPException(
            status_code=401,
            detail="Invalid authentication scheme"
        )
    
    payload = verify_token(token)

    if not payload:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )
    
    return payload


def require_role(allowed_roles: list):

    def role_checker(current_user = Depends(get_current_user)):

        print("ROLE CHECKER")
        print(current_user)

        if current_user["role"] not in allowed_roles:

            raise HTTPException(
            status_code=403,
            detail="Not enough permissions"
            )
        
        return current_user
    
    return role_checker

