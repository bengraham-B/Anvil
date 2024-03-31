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

    id = 1
    name = "Test"
    age = 23

    cursor.execute(f"INSERT INTO your_table_name (id, name, age) VALUES ('{id}', '{name}', '{age}')")

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

    return jsonify(data)
