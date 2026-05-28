from fastapi import APIRouter
from app.controllers.comments_controller import (
    post_new_comment,
    get_ticket_comments
)
from app.schemas.comments_schema import CommentCreate

router = APIRouter(prefix="/tickets")

@router.post("/{ticket_id}/comments")
def post_comment(ticket_id: str, comment: CommentCreate):
    
    print("entro a la route de comments")
    return post_new_comment(ticket_id, comment)


#probando ruta post comment
# {
#     created_by: 22222222-2222-2222-2222-222222222222,
#     message: "probar con resetear router"
# }

@router.get("/{ticket_id}/comments")
def get_all_comments(ticket_id: str):
    
    print("entro a la route de get comments")
    return get_ticket_comments(ticket_id)

