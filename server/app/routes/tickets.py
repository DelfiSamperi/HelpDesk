from fastapi import APIRouter
from app.controllers.tickets_controller import (
    get_all_tickets,
    get_ticket_by_id,
    create_ticket,
    update_ticket
)
from app.schemas.ticket_schema import TicketCreate, TicketUpdate 

router = APIRouter(prefix="/tickets")

@router.get("/")
def get_tickets():
    
    return get_all_tickets()


@router.get("/{id}")
def get_ticket(id: str):

    return get_ticket_by_id(id)


@router.post("/")
def post_ticket(ticket: TicketCreate):
    
    return create_ticket(ticket)


@router.put("/{id}")
def update_ticket_route(id: str, ticket: TicketUpdate):

    return update_ticket(id, ticket)

