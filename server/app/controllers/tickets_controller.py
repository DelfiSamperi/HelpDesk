from app.queries.tickets_queries import (
    fetch_all_tickets,
    fetch_ticket_by_id,
    insert_ticket,
    update_ticket
) 


def get_all_tickets():

    tickets = fetch_all_tickets()

    return {
        "ok": True,
        "data": tickets
    }


def get_ticket_by_id(id):

    ticketById = fetch_ticket_by_id(id)

    return {
        "ok": True,
        "data": ticketById
    }


def create_ticket(ticket):

    new_ticket = insert_ticket(ticket)

    return {
        "ok": True,
        "data": new_ticket
    }


def update_ticket(id, ticket):
    
    ticket_updated = update_ticket(id, ticket)

    return {
        "ok": True,
        "data": ticket_updated
    }

