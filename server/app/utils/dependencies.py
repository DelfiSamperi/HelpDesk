from fastapi import Header, HTTPException

from app.utils.auth import verify_token

def get_current_user(authorization: str = Header(None)):
    
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