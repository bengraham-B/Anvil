from flask import Flask,jsonify,request
import psycopg2

from database import DB_conn
from date import formate_date_anvil

def insert(user_id, details, category, amount, class_, date, day, month, month_text, year):
    print(date)
    print("88888888888888888")
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

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO transaction (user_id, details, category, amount, class, date, day, month, month_text, year) VALUES ('{user_id}', '{details}', '{category}', '{float(amount)}', '{class_}', '{date}', '{day}', '{month}', '{month_text}', '{year}')")
    # print(date_dict["day"])

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
