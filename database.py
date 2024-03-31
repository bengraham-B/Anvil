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

    # Establishing the connection
    conn = psycopg2.connect(
        dbname=db_name,
        user=db_user,
        password=db_password,
        host=db_host,
        port=db_port
    )

    return conn

    # cursor = conn.cursor()

    # cursor.execute("CREATE TABLE test1 (id INT);")

    # create_table_query = '''
    # CREATE TABLE IF NOT EXISTS your_table_name (
    #     id SERIAL PRIMARY KEY,
    #     name VARCHAR(255),
    #     age INT
    # )
    # '''

    # Executing the SQL query to create the table
    # cursor.execute(create_table_query)

    # # Committing the changes
    # conn.commit()

    # cursor.close()
    # conn.close()
