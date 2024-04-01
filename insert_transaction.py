from flask import Flask,jsonify,request
from database import DB_conn
import psycopg2


def insert():
    conn = DB_conn()
    '''
        This function handles inserting transactions intothe DB.
    '''
    print("insert function")

    cursor = conn.cursor()

    user_id = '1234332'
    details = 'purchase new cards'
    category = 'Magic The Gathering'
    amount = 1705
    class_ = 'debit'

    cursor.execute(f"INSERT INTO transactions (user_id, details, category, amount, class) VALUES ('{user_id}', '{details}', '{category}', '{amount}', '{class_}')")

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
