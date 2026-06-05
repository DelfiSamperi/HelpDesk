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

@router.get(
    "/",
    summary="Get all tickets",
    description="""
    Returns a paginated list of tickets.

    - Users can only see their own tickets.
    - Tech and Admin users can see all tickets. 
    """, 
    responses={
        200: {"description": "Tickets retrieved successfully"},
        401: {"description": "Unauthorized"},
        403: {"description": "Forbidden"}
    }  
) # GET /tickets?page=1&limit=12
def get_tickets(
    page: int = 1,
    limit: int= 12,
    current_user = Depends(get_current_user)):
    
    print(current_user)
    return get_all_tickets(current_user, page, limit)


@router.get(
    "/{id}",
    summary="Get ticket by id",
    description="""
    Returns all the info from a selected ticket if the user has access to it.

    - Title
    - Description and comments
    - Status
    - Priority
    - Created by
    - Assigned to
    - Category
    """
)
def get_ticket(id: str, current_user = Depends(get_current_user)):

    return get_ticket_by_id(id, current_user)


@router.get(
    "/{id}/history",
    summary="Get ticket history",
    description="""
    Returns all recorded changes made to a ticket.

    Access is restricted according to the user's role and ticket ownership.
    """
)
def get_ticket_history(id: str, current_user = Depends(get_current_user)):

    return get_ticket_history_by_id(id, current_user)


@router.post(
    "/",
    summary="Create new ticket",
    description="""
    All users can create a new ticket.
"""
)
def post_ticket(
    ticket: TicketCreate,
    current_user = Depends(get_current_user)
):
    print(current_user)
    return create_ticket(ticket, current_user["sub"])


@router.put(
    "/{id}",
    summary="Update ticket",
    description="""
    Authorized users can update ticket info:
    
    - Tech can take a ticket, change priority, status and category.
    - Admin can assign ticket to different tech users and change status, priority and category.
    """
)
def update_ticket_route(
    id: str,
    ticket: TicketUpdate,
    current_user = Depends(
        require_role(["tech", "admin"])
    )
):

    return update_ticket(id, ticket, current_user)

