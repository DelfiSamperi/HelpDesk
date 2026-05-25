from fastapi import APIRouter
from app.controllers.tickets_controller import get_all_tickets
from app.controllers.tickets_controller import get_ticket_id

router = APIRouter(prefix="/tickets")

@router.get("/")
def get_tickets():
    
    print("entro a la route")
    return get_all_tickets()


@router.get("/{id}")
def get_ticket_by_id(id: str):

    print("entro en ruta by ID")
    return get_ticket_id(id)

