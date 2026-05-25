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
    print(ticket)

    cursor.close()
    conn.close()

    return ticket