from app.queries.tickets_queries import (
    fetch_all_tickets,
    fetch_ticket_by_id,
    insert_ticket_to_db,
    update_ticket_to_db
) 

# GET
def get_all_tickets():

    tickets = fetch_all_tickets()

    return {
        "ok": True,
        "data": tickets
    }


# GET by id
def get_ticket_id(id):

    ticketById = fetch_ticket_by_id(id)

    return {
        "ok": True,
        "data": ticketById
    }


# POST
def post_new_ticket(ticket):

    new_ticket = insert_ticket_to_db(ticket)

    return {
        "ok": True,
        "data": new_ticket
    }


# UPDATE
def update_ticket(id, ticket):
    
    ticket_updated = update_ticket_to_db(id, ticket)

    return {
        "ok": True,
        "data": ticket_updated
    }


# DELETE
#def delete_ticket(id):

