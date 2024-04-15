from flask import Flask,jsonify,request
import psycopg2

from database import DB_conn
from date import formate_date_anvil

def insert(user_id, details, category, amount, class_, date):
    conn = DB_conn()
    '''
        This function handles inserting transactions intothe DB.
    '''

    # Checking if the amount value is a Float
    if type(amount) is not float:
        data = {
            "status": "400",
            "message": "Amount is not float"
        }
        return data

    print("insert function")

    print(date, "-----------")

    # Handle inserting Month and Day values
    date_dict = formate_date_anvil(date)

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO transaction (user_id, details, category, amount, class, date, month, year) VALUES ('{user_id}', '{details}', '{category}', '{float(amount)}', '{class_}', '{date}', '{date_dict.month}', '{date_dict.year}')")

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
