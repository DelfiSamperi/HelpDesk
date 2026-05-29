from app.db.connection import get_connection

def fetch_all_comments(ticket_id):

    conn = get_connection()
    cursor = conn.cursor()
    
    #una rutita bien general
    # cursor.execute("""
    #     SELECT *
    #     FROM comments
    #     WHERE ticket_id = %s
    #     ORDER BY created_at ASC
    # """, (ticket_id,))
    
    #ahora una ruta seria
    cursor.execute("""
        SELECT
            comments.id,
            comments.message,
            comments.created_at,
            users.user_name AS author,
            users.user_role
        FROM comments
        JOIN users
        ON comments.created_by = users.id
        WHERE comments.ticket_id = %s
        ORDER BY comments.created_at ASC
""", (ticket_id,))

    comments = cursor.fetchall()
    #log temporal para ver que trae en consola
    print("query que trae comments")
    print(comments)

    cursor.close()
    conn.close()

    return comments


def insert_comment(ticket_id, comment):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO comments (
                   ticket_id,
                   created_by,
                   message
                )
        VALUES (%s, %s, %s)
        RETURNING *
    """, (
        ticket_id,
        comment.created_by,
        comment.message
    ))
    
    new_comment = cursor.fetchone()
    
    print("query comment creado:")
    print(new_comment)

    conn.commit() #obligatorio en insert-update-delete

    cursor.close()
    conn.close()

    return new_comment
