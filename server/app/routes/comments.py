from fastapi import APIRouter
from app.controllers.comments_controller import create_comment, get_ticket_comments
from app.schemas.comments_schema import CommentCreate

router = APIRouter(prefix="/tickets")

@router.post("/{ticket_id}/comments")
def post_comment(ticket_id: str, comment: CommentCreate):
    
    return create_comment(ticket_id, comment)


@router.get("/{ticket_id}/comments")
def get_all_comments(ticket_id: str):
    
    return get_ticket_comments(ticket_id)

