from fastapi import APIRouter, Depends
from app.controllers.tickets_controller import (
    get_all_tickets,
    get_ticket_by_id,
    create_ticket,
    update_ticket,
    get_ticket_history_by_id
)
from app.schemas.ticket_schema import TicketCreate, TicketUpdate 
from app.utils.dependencies import get_current_user, require_role

router = APIRouter(
    prefix="/tickets",
    tags=["Tickets"]
)

@router.get("/") # GET /tickets?page=1&limit=12
def get_tickets(
    page: int = 1,
    limit: int= 12,
    current_user = Depends(get_current_user)):
    
    print(current_user)
    return get_all_tickets(current_user, page, limit)


@router.get("/{id}")
def get_ticket(id: str, current_user = Depends(get_current_user)):

    return get_ticket_by_id(id, current_user)


@router.get("/{id}/history")
def get_ticket_history(id: str, current_user = Depends(get_current_user)):

    return get_ticket_history_by_id(id, current_user)


@router.post("/")
def post_ticket(
    ticket: TicketCreate,
    current_user = Depends(get_current_user)
):
    print(current_user)
    return create_ticket(ticket, current_user["sub"])


@router.put("/{id}")
def update_ticket_route(
    id: str,
    ticket: TicketUpdate,
    current_user = Depends(
        require_role(["tech", "admin"])
    )
):

    return update_ticket(id, ticket, current_user)

