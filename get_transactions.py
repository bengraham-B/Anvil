from database import DB_conn
import psycopg2

def get_transactions(user_id):
    '''
        This function handles getting the user's transactions
    '''
    conn = DB_conn()

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM transaction WHERE user_id='{user_id}'")

    records = cursor.fetchall()

    records_array = []

    for record in records:
        data = {
            "id": record[0],
            "user_id": record[1],
            "details": record[2],
            "amount": record[3],
            "category": record[4],
            "class": record[5],
            "date": record[6],
            "month": record[7],
            "year": record[8],
            "day": record[9]
        }
        records_array.append(data)
    print("----------")
    print(records_array[0])
    print("----------")

    cursor.close()
    conn.close()

    return records_array

