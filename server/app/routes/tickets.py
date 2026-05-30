from fastapi import APIRouter, Depends
from app.controllers.tickets_controller import (
    get_all_tickets,
    get_ticket_by_id,
    create_ticket,
    update_ticket
)
from app.schemas.ticket_schema import TicketCreate, TicketUpdate 
from app.utils.dependencies import get_current_user

router = APIRouter(prefix="/tickets")

@router.get("/")
def get_tickets():
    
    return get_all_tickets()


@router.get("/{id}")
def get_ticket(id: str):

    return get_ticket_by_id(id)


@router.post("/")
def post_ticket(
    ticket: TicketCreate,
    current_user = Depends(get_current_user)
):
    print(current_user)
    return create_ticket(ticket, current_user["sub"])


@router.put("/{id}")
def update_ticket_route(id: str, ticket: TicketUpdate, current_user = Depends(get_current_user)):

    return update_ticket(id, ticket, current_user["sub"])

