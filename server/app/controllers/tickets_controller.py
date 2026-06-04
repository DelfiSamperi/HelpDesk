from fastapi import HTTPException
import math
from app.queries.tickets_queries import (
    fetch_all_tickets,
    count_tickets,
    fetch_ticket_by_id,
    insert_ticket,
    update_ticket_db,
    fetch_ticket_history
) 
from app.queries.users_queries import fetch_user_by_id

#funcion auxiliar
def validate_ticket_access( ticket_id, current_user):
     
    ticket = fetch_ticket_by_id(ticket_id)

    if not ticket:
          
        raise HTTPException(
            status_code=404,
            detail="Ticket not found"
        )
     
    if (current_user["role"] == "user"
        and str(ticket["created_by"]) != current_user["sub"]
    ):
                raise HTTPException(
                    status_code=403,
                    detail="Not enough permissions"
                )
    
    return ticket


def get_all_tickets(current_user, page, limit):

    offset = (page - 1) * limit

    role = current_user["role"]
    user_id = current_user["sub"]

    tickets = fetch_all_tickets(role, user_id, limit, offset)

    total_tickets = count_tickets(role, user_id)

    total_pages = math.ceil(total_tickets / limit)

    return {
        "ok": True,
        "page": page,
        "limit": limit,
        "total_tickets": total_tickets,
        "total_pages": total_pages,
        "data": tickets
    }


def get_ticket_by_id(id, current_user):

    ticket = validate_ticket_access( id, current_user)

    return {
        "ok": True,
        "data": ticket
    }


def get_ticket_history_by_id(ticket_id, current_user):

    validate_ticket_access(ticket_id, current_user)

    ticket_history = fetch_ticket_history(ticket_id)

    return {
        "ok": True,
        "data": ticket_history
    }


def create_ticket(ticket, user_id):

    new_ticket = insert_ticket(ticket, user_id)

    return {
        "ok": True,
        "data": new_ticket
    }


def update_ticket(ticket_id, ticket, current_user):
    
    if ticket.assigned_to is not None:
         
        assigned_user = fetch_user_by_id( ticket.assigned_to)

        if not assigned_user:
             
            raise HTTPException(
                status_code=404,
                deatil="Assigned user not found"
            )
        
        if assigned_user["user_role"] != "tech":
             
            raise HTTPException(
                status_code=400,
                detail="Tickets can only be assigned to tech users"
            )
        
        if (
            current_user["role"] == "tech"
            and str(ticket.assigned_to) != current_user["sub"]
        ):
             
            raise HTTPException(
                status_code=403,
                detail="Tech users can only assign tickets to themselves"
            )
        
    ticket_updated = update_ticket_db(ticket_id, ticket, current_user["sub"])

    return {
        "ok": True,
        "data": ticket_updated
    }

