from app.db.connection import get_connection

#registro de usuarios
def insert_user(user_name, email, hashed_password):
    
    conn = get_connection()
    cursor = conn.cursor()
    
    #creo el user
    cursor.execute("""
        INSERT INTO users (
            user_name,
            email,
            password_hash
        )
        VALUES (%s, %s, %s)
        RETURNING *
    """, (
        user_name,
        email,
        hashed_password
    ))
    
    new_user = cursor.fetchone()

    print("query del usuario registrado:")
    print(new_user)

    conn.commit() #obligatorio en insert-update-delete

    cursor.close()
    conn.close()

    return new_user


#login
def get_user_by_email(email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE email = %s       
    """, (email,))

    user = cursor.fetchone()

    print("query del login de usuario:")
    print(user)

    cursor.close()
    conn.close()

    return user