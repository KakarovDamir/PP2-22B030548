import psycopg2
from config import host, user, password, db, port


try:
    #connection to exist database
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password ,
        database = db,
        port = port
    )
    connection.autocommit = True

    # the cursor for performing database opirations 
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        print(f"Server version: {cursor.fetchone()}")


    with connection.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE PhoneBook(
            Name varchar(255) NOT NULL,
            Number INTEGER NOT NULL)"""
        )
        print("[INFO]: Table created successfully")     


except (Exception, psycopg2.DatabaseError) as error:
    print(error)


finally:
    if connection:
        connection.close()
        print("[INFO]:PostgreSQL connection closed")