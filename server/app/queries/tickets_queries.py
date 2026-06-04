from app.db.connection import get_connection

def fetch_all_tickets(role, user_id, limit, offset):

    conn = get_connection()
    cursor = conn.cursor()

    if role in ["tech", "admin"]:

        cursor.execute("""
            SELECT *
            FROM ticket
            ORDER BY created_at DESC
            LIMIT %s
            OFFSET %s
        """, (
            limit,
            offset
        ))

    else:

        cursor.execute("""
            SELECT *
            FROM ticket
            WHERE created_by = %s
            ORDER BY created_at DESC
            LIMIT %s
            OFFSET %s
        """, (user_id, limit, offset))
    
    tickets = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return tickets


def count_tickets(role, user_id,):

    conn = get_connection()
    cursor = conn.cursor()

    if role in ["tech", "admin"]:

        cursor.execute("""
            SELECT COUNT(*)
            FROM ticket
        """
        )

    else:

        cursor.execute("""
            SELECT *
            FROM ticket
            WHERE created_by = %s
        """, (user_id,))

    total_tickets = cursor.fetchone()["count"]

    cursor.close()
    conn.close()

    return total_tickets


def fetch_ticket_by_id(id):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM ticket
        WHERE id = %s
    """, (id,))
    
    ticket = cursor.fetchone()
        
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


def update_ticket_db(id, ticket, user_id):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
            FROM ticket
            WHERE  id = %s
        """, (id,))
    
    old_ticket = cursor.fetchone()
    print(old_ticket)

    if not old_ticket:
        cursor.close()
        conn.close()
        return None

    fields = []
    values = []
    changes = []

    if (
        ticket.status is not None
        and ticket.status != old_ticket["status"]
    ):
        fields.append("status = %s")
        values.append(ticket.status)
        changes.append({
            "field": "status",
            "old_value": old_ticket["status"],
            "new_value": ticket.status
        })

    if (
        ticket.priority is not None
        and ticket.priority != old_ticket["priority"]
    ):
        fields.append("priority = %s")
        values.append(ticket.priority)
        changes.append({
            "field": "priority",
            "old_value": old_ticket["priority"],
            "new_value": ticket.priority
        })

    if (
        ticket.assigned_to is not None
        and ticket.assigned_to != old_ticket["assigned_to"]
    ):
        fields.append("assigned_to = %s")
        values.append(ticket.assigned_to)
        changes.append({
            "field": "assigned_to",
            "old_value": str(old_ticket["assigned_to"]),
            "new_value": str(ticket.assigned_to)
        })

    if (
        ticket.category_id is not None
        and ticket.category_id != old_ticket["category_id"]
    ):
        fields.append("category_id = %s")
        values.append(ticket.category_id)
        changes.append({
            "field": "category_id",
            "old_value": str(old_ticket["category_id"]),
            "new_value": str(ticket.category_id)
        })

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

    cursor.execute(query, tuple(values))

    updated_ticket = cursor.fetchone()

    for change in changes:

        cursor.execute("""
            INSERT INTO ticket_history (
                ticket_id,
                changed_by,
                field,
                old_value,
                new_value
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            id,
            user_id,
            change["field"],
            change["old_value"],
            change["new_value"]
        ))
    
    conn.commit() #obligatorio en insert-update-delete

    print('ticket updated')

    cursor.close()
    conn.close()

    return updated_ticket


def fetch_ticket_history(ticket_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            th_id,
            th.ticket_id,
            th.old_value,
            th.new_value,
            th.created_at,
            u.user_name AS changed_by
        FROM ticket_history th
        JOIN users u
            ON th.changer_by = u.id
        WHERE th.ticket_id = %s
        ORDER BY th.created_at DESC
        """, (ticket_id,))
    
    ticket_history = cursor.fetchall()

    cursor.close()
    conn.close()
    
    return ticket_history
    
