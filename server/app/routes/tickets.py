from fastapi import APIRouter
from app.controllers.tickets_controller import (
    get_all_tickets,
    get_ticket_id,
    post_new_ticket,
    update_ticket
)

from app.schemas.ticket_schema import (
    TicketCreate,
    TicketUpdate
) 


router = APIRouter(prefix="/tickets")

@router.get("/")
def get_tickets():
    
    print("entro a la route")
    return get_all_tickets()


@router.get("/{id}")
def get_ticket_by_id(id: str):

    print("entro en ruta by ID")
    return get_ticket_id(id)


@router.post("/")
def post_ticket(ticket: TicketCreate):
    
    print("route posting new ticket")
    return post_new_ticket(ticket)


# PARA PROBAR LA RUTA POST
# {
#   "title": "VPN no conecta",
#   "description": "El usuario no puede conectarse a la VPN desde su hogar desde esta mañana.",
#   "priority": "high",
#   "created_by": "3cccc33c-cc3c-3333-3cc3-cccc33333333",
#   "category_id": 2
# }

@router.put("/{id}")
def update_ticket_route(id: str, ticket: TicketUpdate):

    print("updating ticket")
    return update_ticket(id, ticket)

