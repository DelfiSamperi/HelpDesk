from app.db.connection import get_connection

def fetch_all_tickets():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM ticket
        ORDER BY created_at DESC
    """)
    
    tickets = cursor.fetchall()
    
    print(tickets)

    cursor.close()
    conn.close()

    return tickets


def fetch_ticket_by_id(id):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM ticket
        WHERE id = %s
    """, (id,))
    
    ticket = cursor.fetchone()
        
    print(ticket)

    cursor.close()
    conn.close()

    return ticket


def insert_ticket(ticket, user_id):
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("""
        INSERT INTO ticket (
            title,
            description,
            priority,
            created_by,
            category_id
        )
        VALUES (%s, %s, %s, %s, %s)
        RETURNING *
    """, (
        ticket.title,
        ticket.description,
        ticket.priority,
        user_id,
        ticket.category_id
    ))
    
    new_ticket = cursor.fetchone()

    print(new_ticket)

    #creo el comment inicial automaticamente (description)
    cursor.execute("""
        INSERT INTO comments (
            ticket_id,
            created_by,
            message
        )
        VALUES (%s, %s, %s)
    """, (
    new_ticket["id"], 
    user_id,
    ticket.description
    ))

    #confirma transaccion
    conn.commit() #obligatorio en insert-update-delete

    cursor.close()
    conn.close()

    return new_ticket


def update_ticket_db(id, ticket):
    
    conn = get_connection()
    cursor = conn.cursor()

    fields = []
    values = []

    if ticket.status is not None:
        fields.append("status =%s")
        values.append(ticket.status)

    if ticket.priority is not None:
        fields.append("priority = %s")
        values.append(ticket.priority)

    if ticket.assigned_to is not None:
        fields.append("assigned_to = %s")
        values.append(ticket.assigned_to)

    if ticket.category_id is not None:
        fields.append("category_id = %s")
        values.append(ticket.category_id)

    if not fields:
        return None

    set_clause = ", ".join(fields) #une campos dinamicamente

    query = f"""
        UPDATE ticket
        SET {set_clause}
        WHERE id = %s
        RETURNING *
    """
    values.append(id) #agrega id al final

    print('ticket updated:')
    print(query)
    print(values)

    cursor.execute(query, tuple(values))

    updated_ticket = cursor.fetchone()
    
    conn.commit() #obligatorio en insert-update-delete

    cursor.close()
    conn.close()

    return updated_ticket

