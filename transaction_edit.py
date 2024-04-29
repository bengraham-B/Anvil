from database import DB_conn 
import psycopg2 

from date import formate_date_anvil

def edit_transaction(details, amount, category, _class, date, user_id, transaction_id):
    print(date)
    print("00000000000000000000000000000")
    print("Edit Transaction Function")

    conn = DB_conn()

    # date_dict = formate_date_anvil(date=date)

    cursor = conn.cursor()
    SQL = f"""
        UPDATE transaction 
        SET 
            details = '{details}',
            amount = '{amount}',
            category = '{category}',
            class = '{_class}',
            date = '{date}'

        WHERE 
            user_id = '{user_id}' and id='{transaction_id}';
    """
    cursor.execute(SQL)

    conn.commit()
    cursor.close()
    conn.close()

    print("Transaction Successfully Update")
    return 200



