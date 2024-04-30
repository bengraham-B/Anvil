from database import DB_conn
import psycopg2

def get_transactions(user_id):
    '''
        This function handles getting the user's transactions
    '''
    conn = DB_conn()

    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM transaction WHERE user_id='{user_id}' ORDER BY date DESC")

    records = cursor.fetchall()

    records_array = []

    # {
    #     0'id': 'f70c7276-ce37-412b-ad98-c096fb0a611e', 
    #     1'user_id': 'bn-33', 
    #     2'details': 'food ', 
    #     3'amount': 43.0, 
    #     4'category': 
    #     5'freeman', 
    #     6'class': 'I', 
    #     7'date': datetime.date(2024, 4, 12), 
    #     8'day': 12, 
    #     9'month_text': 3, 
    #     10'month': 'Apr', 
    #     11'year': 2024
    # }

    for record in records:
        data = {
            "id": record[0],
            "user_id": record[1],
            "details": record[2],
            "amount": record[3],
            "category": record[4],
            "class": record[5],
            "date": record[6],
            "day": record[7],
            "month": record[8],
            "month_text": record[9],
            "year": record[10]
        }
        records_array.append(data)

    # print(records_array[0])
    cursor.close()
    conn.close()

    return records_array

