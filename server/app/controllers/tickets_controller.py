from fastapi import HTTPException
from app.queries.tickets_queries import (
    fetch_all_tickets,
    fetch_ticket_by_id,
    insert_ticket,
    update_ticket_db
) 


def get_all_tickets(current_user):

    role = current_user["role"]
    user_id = current_user["sub"]

    tickets = fetch_all_tickets(role, user_id)

    return {
        "ok": True,
        "data": tickets
    }


def get_ticket_by_id(id, current_user):

    ticket_by_id = fetch_ticket_by_id(id)

    if not ticket_by_id:

        raise HTTPException(
            status_Code=404,
            detail="Ticket not found"
        )
    
    role = current_user["role"]
    user_id = current_user["sub"]

    if role == "user":

        if str(ticket_by_id["created_by"]) != user_id:

            raise HTTPException(
                status_code=403,
                detail="Not enough permissions"
            )

    return {
        "ok": True,
        "data": ticket_by_id
    }


def create_ticket(ticket, user_id):

    new_ticket = insert_ticket(ticket, user_id)

    return {
        "ok": True,
        "data": new_ticket
    }


def update_ticket(id, ticket, user_id):
    
    ticket_updated = update_ticket_db(id, ticket)

    return {
        "ok": True,
        "data": ticket_updated
    }

