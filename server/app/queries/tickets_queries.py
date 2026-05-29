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
    #log temporal para ver que trae en consola
    print("query trae todos los tickets")
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
    #log temporal para ver que trae en consola
    print("query traer ticket by id")
    print(ticket)

    cursor.close()
    conn.close()

    return ticket


def insert_ticket_to_db(ticket):
    
    conn = get_connection()
    cursor = conn.cursor()
    
    #creo el ticket
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
        ticket.created_by,
        ticket.category_id
    ))
    
    new_ticket = cursor.fetchone()

    print("aca estamos en la query, ticket creado:")
    print(new_ticket)

    #creo el comment inciial automaticamente (description)
    cursor.execute("""
        INSERT INTO comments (
            ticket_id,
            created_by,
            message
        )
        VALUES (%s, %s, %s)
    """, (
    new_ticket["id"], #id del ticket recien creado
    ticket.created_by,
    ticket.description
    ))

    print("comment incial creado")
    
    #confirma transaccion
    conn.commit() #obligatorio en insert-update-delete

    cursor.close()
    conn.close()

    return new_ticket


def update_ticket_to_db(id, ticket):
    
    conn = get_connection()
    cursor = conn.cursor()

    print("query update ticket")

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

