import psycopg2

def DB_conn():
    '''
    This function handles connecting to the database
    '''

    db_name = "anvil"
    db_user = "root"
    db_password = "root"
    db_host = "localhost"
    db_port = 5429

    conn = None

    try:
        # Establishing the connection
        conn = psycopg2.connect(
            dbname=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port
        )

        # Check if the connection is successful by executing a simple query
        cursor = conn.cursor()
        cursor.execute("SELECT 1")
        cursor.close()

        print("Connection successful!")

    except psycopg2.Error as e:
        print(f"Error connecting to the database: {e}")
        if conn:
            conn.close()

    return conn
