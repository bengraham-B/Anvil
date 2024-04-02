from flask import Flask,jsonify,request
from database import DB_conn
import psycopg2


def insert(user_id, details, category, amount, class_):
    conn = DB_conn()
    '''
        This function handles inserting transactions intothe DB.
    '''
    print("insert function")

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO transaction (user_id, details, category, amount, class) VALUES ('{user_id}', '{details}', '{category}', '{int(amount)}', '{class_}')")

    # Committing the changes
    conn.commit()

    # Closing the cursor and connection
    cursor.close()
    conn.close()

    print("Query Done!")
    data = {
        "status": 200,
        "message": "Success Insert transaction"
    }

    return data
