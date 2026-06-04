from app.db.connection import get_connection

def update_user_role(user_id, role):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE users
        SET user_role = %s
        WHERE id = %s
        RETURNING *                   
    """, (
        role,
        user_id
    ))

    user_role = cursor.fetchone()

    print("query de reasignacion de rol de usuario:")
    print("New role: ", user_role)

    conn.commit()

    cursor.close()
    conn.close()

    return user_role


def fetch_all_users(limit, offset):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            user_name,
            email,
            user_role,
            active,
            created_at
        FROM users
        ORDER BY created_at DESC
        LIMIT %s
        OFFSET %s
    """, (
        limit,
        offset
    ))

    users = cursor.fetchall()

    print(users)
    
    cursor.close()
    conn.close()

    return users


def count_users():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM users
    """
    )

    total_users = cursor.fetchone()["count"]

    cursor.close()
    conn.close()

    return total_users


def fetch_user_by_id(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            user_name,
            email,
            user_role,
            active,
            created_at
        FROM users
        WHERE id = %s
    """, (id,))
    
    user_id = cursor.fetchone()

    print(user_id)

    cursor.close()
    conn.close()

    return user_id

