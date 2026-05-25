from app.queries.tickets_queries import fetch_all_tickets
from app.queries.tickets_queries import fetch_ticket_by_id

def get_all_tickets():

    tickets = fetch_all_tickets()

    return {
        "ok": True,
        "data": tickets
    }


def get_ticket_id(id):

    ticket = fetch_ticket_by_id(id)

    return {
        "ok": True,
        "data": ticket
    }

