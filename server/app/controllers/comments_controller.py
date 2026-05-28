from app.queries.comments_queries import (
    fetch_all_comments,
    insert_comment
) 

# GET
def get_ticket_comments(ticket_id):

    comments = fetch_all_comments(ticket_id)

    return {
        "ok": True,
        "data": comments
    }


# POST
def post_new_comment(ticket_id, comment):

    new_comment = insert_comment(ticket_id, comment)

    return {
        "ok": True,
        "data": new_comment
    }
