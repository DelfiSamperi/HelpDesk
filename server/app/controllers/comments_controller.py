from app.queries.comments_queries import fetch_comments_by_ticket, insert_comment

def get_ticket_comments(ticket_id):

    comments = fetch_comments_by_ticket(ticket_id)

    return {
        "ok": True,
        "data": comments
    }


def create_comment(ticket_id, comment):

    new_comment = insert_comment(ticket_id, comment)

    return {
        "ok": True,
        "data": new_comment
    }
