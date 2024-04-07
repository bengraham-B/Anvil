from database import DB_conn
import psycopg2

def get_categories_db(user_id):
    '''
        Gets all categories by user_id
    '''

    conn = DB_conn()

    cursor = conn.cursor()

    
    cursor.execute(f"SELECT * FROM categories WHERE user_id = ('{user_id}')")
    
    categories = cursor.fetchall()

    

    category_array = []

    for cat in categories:
        data = {
            "id": cat[0],
            "name": cat[1],
            "user_id": [2]
        }

        category_array.append(data)
        

    return category_array
