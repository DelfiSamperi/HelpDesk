from fastapi import APIRouter, Depends
from app.controllers.comments_controller import create_comment, get_ticket_comments
from app.schemas.comments_schema import CommentCreate
from app.utils.dependencies import get_current_user

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
    )

@router.post(
    "/{ticket_id}/comments",
    summary="Post a new comment in a ticket",
    description="""
    Authorized users can add comments to the ticket.

    - User who created the ticket can add comments.
    - Tech who was assigned the ticket can add comments.
    """
)
def post_comment(ticket_id: str, comment: CommentCreate, current_user = Depends(get_current_user)):
    
    return create_comment(ticket_id, comment, current_user["sub"])


@router.get(
    "/{ticket_id}/comments",
    summary="Get all comments from a ticket",
    description="Authorized users can access to all comments from one ticket."    
)
def get_all_comments(ticket_id: str):
    
    return get_ticket_comments(ticket_id)

