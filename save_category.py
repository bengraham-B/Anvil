from database import DB_conn
import psycopg2
def save_category_db(name, user_id):
    '''
    This function gets all the user's categories from the DB.
    '''

    conn = DB_conn()

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO categories (name, user_id) VALUES ('{name}', '{user_id}')")

    conn.commit()

    cursor.close()
    conn.close()

    print("Category Insert Successfully")

    data = {
        "status": 200,
        "message": "Category Saved"
    }
    
    return data
